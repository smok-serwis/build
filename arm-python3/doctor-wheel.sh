#!/bin/bash

#
# A shell script to strip any executables found within Python wheels
#

WHEEL_NAME=$(basename "$1")
MY_DIR="$(cat /proc/sys/kernel/random/uuid)"
mkdir "${MY_DIR}"
mv "$1" "${MY_DIR}"
cd "${MY_DIR}"
unzip "$WHEEL_NAME"
for F in $(find . -iname *.so)
do
  strip -X -x "$F"
done
rm -f "$WHEEL_NAME"
zip -r "$WHEEL_NAME" .
cp "$WHEEL_NAME" ..
cd ..
rm -rf "${MY_DIR}"

