#!/bin/bash

readonly POSTFIX="_temp"
readonly DIFF_FILE="diff"

function recover_target() {
  # branch
  RECOVER=$(git rev-parse --abbrev-ref HEAD)
  if [ "HEAD" = ${RECOVER} ]; then
    # hash
    RECOVER=$(git log -1 --format="%H")
  fi
}

function copy() {
  local TAG=$1
  local TEMP="$TAG$POSTFIX"
  git checkout ${TAG}
  cp -R ./proto ${TEMP}
}

function gen_diff() {
  local LEFT=$1
  local RIGHT=$2
  diff "$LEFT$POSTFIX" "$RIGHT$POSTFIX" > ${DIFF_FILE}
  echo -e "\nDiff file is generated to $DIFF_FILE\n"
}

function remove_temp() {
  local TAG=$1
  local TEMP="$TAG$POSTFIX"
  rm -rf ${TEMP}
}

function main() {
  recover_target
  echo "Current : $RECOVER"

  PRE=$1
  POST=$2
  [ -z $PRE ] && echo "Pre version must not null" && exit -1
  [ -z $POST ] && echo "Post version must not null" && exit -1
  echo "Dumping diff between $PRE and $POST"

  copy ${PRE}
  copy ${POST}

  gen_diff ${PRE} ${POST}

  remove_temp ${PRE}
  remove_temp ${POST}

  git checkout ${RECOVER}
}

main $@
