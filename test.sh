#!/opt/bin/bash


psql -d video_metadata -U postgres -c "select path from video_file v inner join mapper m on v.mapper_id=m.id and m.type='tvshow_episode' left outer join tvshow_episode e on e.mapper_id=m.id where e.mapper_id is NULL; \
" | sed "1,2d; :a; \$d; N; 3,4ba; P; D" | while read a; do 
  echo $a;
  #/var/packages/VideoStation/target/bin/synovideoindex -t videometa -a "$a"; 
  synoindex -d "$a";
  synoindex -a "$a";
done;

