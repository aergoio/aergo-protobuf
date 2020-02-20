#!/bin/bash

PRE=$1
POST=$2
if [ -z $PRE ] || [ -z $POST ]; then
  echo "Usage: ./make_diff.sh v1.3.0 v2.0.0"
  exit -1
fi

DATE=`git log --simplify-by-decoration --pretty="format:%ai %d" | grep "$POST"`
DATE_FORMAT=`date -j -f "%FT%T%z" "${DATE:0:10}T00:00:00+0000" +"%B %-d, %Y"`

if [[ ${POST:0:1} == "v" ]]; then
  HEADING=${POST:1}
else
  HEADING=$POST
fi

echo "## ${HEADING} (${DATE_FORMAT})"
echo
echo '```diff'
git diff -w -U0 $PRE $POST proto | ./format_diff.py
echo '```'