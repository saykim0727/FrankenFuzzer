#!/bin/bash
RAND=$(python -c 'import uuid; print uuid.uuid4()')
target="/FUZZ/pngtopnm"
FILENAME="/FUZZ/pin/result"
FUZZFILE="/tmp/fuzzer"
CASE="/tmp/testcase"
COUNT=0
INS_COUNT=0
BB_COUNT=0
FUZZ="None"
IFS=""
cat $FUZZFILE | \
while read line
do
    FUZZ=$line
    pathCoverage="/FUZZ/share/coverage/"$FUZZ
    /usr/bin/python /FUZZ/monitor.py $FUZZ $CASE
    /FUZZ/pin/pin -t /FUZZ/pin/MyPinTool.so -o $pathCoverage/$RAND -- $target < $CASE
    /usr/bin/sha1sum $pathCoverage/$RAND > /tmp/$RAND
    cat $pathCoverage/$RAND | \
    while read line
    do
        TEMP=$line
        NAME=$(echo ${TEMP%% *})
        mv $pathCoverage/$RAND $pathCoverage/$NAME
    done
    $target < $CASE
    rm $CASE
done
