#!/opt/bin/bash

synoindex -d "$1";
mv "$1" "$2";
synoindex -a "$2";
