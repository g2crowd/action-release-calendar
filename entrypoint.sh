#!/bin/sh -l

cd /opt/app
RESULT="false"

python src/main.py --timezone $1
BUILD_RESULT=$?
if [ $BUILD_RESULT -ne 0 ]; then
  RESULT="true"
else
  RESULT="false"
fi

echo $RESULT
echo ::set-output name=release_freeze::$RESULT
