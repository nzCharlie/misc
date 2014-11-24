#!/opt/bin/bash

psql -d video_metadata -U postgres -c "select path from video_file v inner join mapper m on v.mapper_id=m.id and m.type='movie' left outer join movie e on m.id=e.mapper_id where e.mapper_id is null; ; \
" | sed "1,2d; :a; \$d; N; 3,4ba; P; D"