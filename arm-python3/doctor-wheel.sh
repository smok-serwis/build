#!/bin/bash

MY_DIR="$(cat /proc/sys/kernel/random/uuid)"
mv "$1" "${MY_DIR}"
cd "${MY_DIR}"
unzip "$1"
for F in $(find . -iname *.so)
do
  strip -X -x "$F"
done
rm -f "$1"
zip -r "$1" .
cp "$1" ..
cd ..
rm -rf "${MY_DIR}"
