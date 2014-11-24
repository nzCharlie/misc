find $1 -type f -name "*.mp4" -o -name "*.mkv" -o -name "*.avi" | grep -v 'eaDir' | while read a; do 
  p=`echo $a |
sed "s/'/''/g"`; 
  c=`psql -d 'video_metadata' -U postgres -c "select count(*) from video_file where path='${p}';" | tail -n 3 | head -n 1`; 
  if [ $c -eq 0 ]; then 
    echo $a;  
  fi; 
done;
