#!/opt/bin/bash

if [ ${2: -1} != "/" ]; then
  echo "second arg should end in /";
  exit -1;
fi;

if [ -d "$1" ]; then
  mv -i "$1" "$2";
  synoindex -A "${2}${1}";
elif [ -f "$1" ]; then
  mv -i "$1" "$2";
  synoindex -a "${2}${1}";
else
  echo "${1} does not exist";
fi; 

