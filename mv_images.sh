#!/bin/bash

echo "mv _static to static"
mv blog/html/_static blog/html/static
echo "mv _images to images"
mv blog/html/_images blog/html/images

for file in $(find . -name "*.html")
do
    echo "Replacing on : $file"
    sed 's/_static/static/g' $file > $file.tmp
    sed 's/_images/images/g'  $file.tmp > $file
    rm $file.tmp
    echo "Replacement done on : $file"
done
