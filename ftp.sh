#!/opt/bin/bash

function list()
{
  local path="$1";
  ncftpls -m "$path" | while read a; do
    if [ ${a: -1} == "/" ]; then
      list "${path}${a}";
    else
      echo "${path}${a}";
    fi
  done;
}

list "$1";
