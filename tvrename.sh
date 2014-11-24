#!/opt/bin/bash

find . -type f -maxdepth 1 -name "*.${1}" | grep '\.[0-9][0-9][0-9]\.' | while read a; do 
  new=`echo $a | sed -r 's/\.([0-9])([0-9][0-9])\./.S0\1E\2./'`; 
  ~/bin/rename_video.sh $a $new; 
done;
