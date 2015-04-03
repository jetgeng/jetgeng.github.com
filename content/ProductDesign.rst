产品相关的设计
==============

:date: 2015-3-30 10:20
:modified: 2015-03-31 18:40
:tags: Product
:category: 设计
:authors: Jet Geng
:summary: 产品数据相关的展现

设计目标
--------

 #. 产品能够作用域
 #. 产品是来源于多个数据源
 #. 给前端展现要使用一个统一的格式。

    #. 一组产品的数据格式的内容为：

    .. code-block:: javascript
    
       [{
         name : '长途汽车票',
         type : 'Piao',   //后台系统定义。
         category : '',   //类别  
         id : '',
         title : '',
         desc : '',
         price : '',
         canModifyPrice : true,
         attributes :  {
            //其他属性，图片啥的。
         }
         validate : {
            //前端验证规则
         }

         
       }]
    
#. 所有服务采用组合的方式进行拼装
    





