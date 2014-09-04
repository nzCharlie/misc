#!/opt/bin/bash
while read a; do echo "$a" >&2; cksfv "$a" | fgrep -v '; Generate' | fgrep -v '; Proj'; done < $1 > $2 
 
