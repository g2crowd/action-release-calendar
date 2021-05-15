#!/bin/sh -l

cd /opt/app
RESULT="false"

python src/main.py $1 $2
BUILD_RESULT=$?
if [ $BUILD_RESULT -gt 0 ]; then
  RESULT="true"
else
  RESULT="false"
fi

echo $RESULT
echo ::set-output name=release_freeze::$RESULT
