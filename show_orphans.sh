#!/opt/bin/bash


psql -d video_metadata -U postgres -c "select path from video_file; \
" | sed "1,2d; :a; \$d; N; 3,4ba; P; D" | while read a; do if [ ! -f "$a" ]; then echo $a; fi; done;

