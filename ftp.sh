#!/opt/bin/bash

function list()
{
  local path="$1";
  p=$(ncftpls -m "${path// /%20}");
  
  # turn p into array of file paths for the given $path
  p=("${p// /%20}")
  
  # if the given $path is for a single file then print it
  if [[ ${#p[@]} -eq 1 && ${p[@]} == ${path: $(( -1 * ${#p[0]} ))} ]]; then
    echo "${path}";
  else
    # otherwise for each file path
    for a in ${p[@]}; do
      # extract the last part of the path, the listed in p contains the dir name
      i=$(echo $a | sed -r 's|^.*/([^/]+)/?$|\1|')
      # if path is a dir, list it
      if [ ${a: -1} == "/" ]; then
        list "${path}/${i//%20/ }";
      else
        # otherwise print it 
        echo "${path}/${i//%20/ }";
      fi
    done
  fi
}

list "$1";

