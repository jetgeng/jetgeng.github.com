一段代码演变的故事
==================

.. TODO 
    主要时分析程序的结构为主

前段时间项目需要从一个mysql数据库(记做A库)导入到另外mysql数据库（记做B库)。在到换的过程中需要对数据进行一些转换。本质而言就是把同样的业务数据分成不同的格式进行存储。初期的我们想法很简单，通过如下步骤来完成：
  #. 从老库逐条读取出数据，
  #. 将这些数据拼装成POJO，这些POJO通过ORM框架可以直接存入数据库B
  #. 通过ORM框架将数据逐条出入数据库。

主题的程序结构如下为代码所示:

.. code-block:: java

  public static class DBMigrate{
    public static void main(String[] args) throws Exception{
        //分析参数
        for(int i = 0; i < offset; i++){
            id = startId + i
            pojo = loadOldPOJO(id); //从老库获取POJO
            savePOJO2NewDB(pojo);
        }
    }

    private static loadOldPOJO(int index){
        POJO pojo = new POJO();
        String sql1 = "";
        getRS(sql1) //根据一个Sql查询POJO中的一部分。拼装入pojo
        ............
        ............ //根据不同的sql，重复上面的步骤。

        return pojo
    }

    private static void savePOJO2NewDB(POJO pojo){
        //使用ibatis保存该记录。
        //同时会更新n多表
    }
    
  }

牛x的你可能一眼就能看出我们这个结构中致命的问题--效率！ 逐条导入数据效率会非常底下。一笔数据将要多次连接数据库。另外当前结构还有一个致命缺点就是啥和啥的都混在一起。想要加个表和减少一个表都很困难。

针对上面的问题我们不得不对这段代码做点改动。改动的第一目标就是让他快起来！

加速
----
加速时目标。手段是减少和数据库交互。说白了就是批量处理这个的感谢mysql提供了强大的插入命令。

.. code-block:: mysql

      INSERT [LOW_PRIORITY | DELAYED | HIGH_PRIORITY] [IGNORE]
      [INTO] tbl_name
      [PARTITION (partition_name,...)] 
      [(col_name,...)]
      {VALUES | VALUE} ({expr | DEFAULT},...),(...),...
      [ ON DUPLICATE KEY UPDATE
      col_name=expr
      [, col_name=expr] ... ]

这个命令可以一次插入很多条数据，只要你的sql够长就可以。就像下面的样子：

.. code-block:: sql

  INSERT INTO tbl_name (a,b,c) VALUES(1,2,3),(4,5,6),(7,8,9); 

这样就往数据库中插入了三条记录。1000条也是这样。这个就是我们的核心技术。
为了能够对数据库表批量操作。将不再将老数据拼装中间状态的POJO，直接使用对应于新表的POJO。** 让数据从业务逻辑中解放出来** 
所以就有一些和与B数据库表一一对应的POJO。下面的转换的过程就以这个与B数据库一一对应的表为中心。下面要做的事情就时很老套的了。

 #. 根据POJO从A数据库中获取一批该数据库所需要的。
 #. 拼装成和B数据库表对应的POJO
 #. 使用批量插入语句将POJO插入到新的数据库。

 在上述动作中对每一个表操作的不同点有三点：
  #. 从A数据库获取数据的sql
  #. 将从A数据库获取的数据拼装成对象。
  #. POJO插入到B数据库时，对应的字段。也就是插入方式不同。

只要将上述这个三个地方抽取出来我们就可以用一套代码完成所有表的操作。基于这个思路我们有了如下的代码.

.. uml::

    interface IRecordCallBack{
        +processRecord(ResultSet):T
        +getQuerySql():String
    }

    interface BatchOperate{
        +saveByBatch(list:List<T>):int
    }
        
    class SomePOJODao{
        +saveByBatch(list:List<SomePOJO>):int
    }
    class AnotherPOJODao{
        +saveByBatch(list:List<AnotherPOJO>):int
    }
    class SomePOJORecordCallBack {
        +processRecord(ResultSet):SomePOJO
        +getQuerySql():String
    }

    class AnotherPOJORecordCallBack{
        +processRecord(ResultSet):AnotherPOJO
        +getQuerySql():String
    }

    IRecordCallBack <|-- SomePOJORecordCallBack 
    IRecordCallBack <|-- AnotherPOJORecordCallBack 

    BatchOperate <|--  SomePOJODao
    BatchOperate <|-- AnotherPOJODao


在上图的结构中IRecordCallBack 中的 getQuerySql 方法用于解决如何获取数据的问题。processRecord 方法用于解决如何拼装POJO的问题。
BatchOperate 方法中用于解决如何保存的问题。
这样所有问题都解决了。我们的工作是否完了呢。还没有，还缺少一个总管来协调让这些分散的类协同工作。

程序的拼装
----------
在前期的程序中，我们直接将程序里面。这样如果要加一个表，牵涉的内容会比较多。
我们做了如下改进。同样时以于与数据库B一一对应的POJO为中心创建两个Map，具体代码如下：

.. code-block:: java

        public static Map<Class<?>, IRecordCallBack<?>> callbacks = new HashMap<Class<?>, IRecordCallBack<?>>();
        public static Map<Class<?>, Class<?>[]> daoMap = new HashMap<Class<?>, Class<?>[]>();
        static {
            callbacks.put(SomePOJO.class, new SomePOJORecordCallBack())
            callbacks.put(AnotherPOJODao.class, new AnotherPOJORecordCallBack())
            daoMap.put(SomePOJO.class, SomePOJODao.class)
            daoMap.put(AnotherPOJO.class, AnotherPOJODao.class)
            
        }


有了这样的配置信息后，我们后期的程序根本不许要知道当前处理的时什么pojo。只是知道取数据，交给dao取保存就可以了。下面给出伪代码如下：

.. code-block:: java

     
    private static void startMigrate(int start, int end){
        //获取数据库连接
        for (Map.Entry<Class<?>, IRecordCallBack<?>> tableItem : callbacks.entrySet()) {
            PreparedStatement stmt = conn.prepareStatement(tableItem.getValue().getQuerySql());
            while (rs.next()) {
	            list.add(tableItem.getValue().processRecord(rs));
		    }
            for(Class<?> cls : daoMap.get(tableItem.getKey())){
                BatchOperate dao = (BatchOperate) session.getMapper(cls);
                logger.info("cls.getName():"+cls.getName());
			    if (dao != null&&list.size()!=0) {
				        dao.saveByBatch(list);
			    }
			}
            //各种善后
            //小睡一会
        }
    }

这个就是所有改善后的结果。这样改动后效率提升了不少。结构上也把重复的代码去掉。今后如果要加入新的数据库表的话，只需要实现一个POJO, IRecordCallBack 和Dao就可以了。其他东西都不用动了。

扩展,插件化
------------

到这里应该说告一段落了。但是还没有完。现在的情况如果你要添加一个表的导入的话。你还的修改daoMap和callBacks这两个map。

其实我们这边很容易通过 `SPI <http://en.wikipedia.org/wiki/Service_provider_interface>`_  将IRecordCallBack 和BatchOperate 服务化。通过 java.util.ServiceLoader 来动态获取当前系统中已经存在的实现。动态创建daoMap和callbacks，这样就建立起了一个可管理插件的框。

.. note:: 

    某个牛人说过：写软件就是在别人写的框子里填数，或则自己写框让别人填数。

我们只是做好了让别人(包括我们自己)填的框！
    
    



































.. author:: default
.. categories:: none
.. tags:: none
.. comments::
