#!/bin/bash

PRE=$1
POST=$2
if [ -z $PRE ] || [ -z $POST ]; then
  echo "Usage: ./make_diff.sh v1.3.0 v2.0.0"
  exit -1
fi

git diff -w -U0 $PRE $POST proto | ./format_diff.py