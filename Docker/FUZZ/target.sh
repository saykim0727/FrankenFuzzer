#!/bin/bash
RANDOM=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | sed 1q)
target="/FUZZ/afl_test_t_false"
FILENAME="/FUZZ/pin/result"
COUNT=0
INS_COUNT=0
BB_COUNT=0
cat $FILENAME | \
while read line      
do
    if [ $COUNT -eq 0 ]; then
        INS_COUNT=$line
        COUNT=1
    else
        BB_COUNT=$line
        COUNT=0
    fi
done
/FUZZ/pin/pin -t /FUZZ/pin/MyPinTool.so -o /FUZZ/pin/result -- $target $@
cat /FUZZ/pin/result | \
while read line
do
    if [ $COUNT -eq 0 ]; then
        if [ $line -gt $INS_COUNT ]; then
            echo $@ > /FUZZ/share/seed/$RANDOM
        fi
        COUNT=1
    else
        if [ $line -gt $BB_COUNT ]; then
            echo $@ > /FUZZ/share/seed/$RANDOM
        fi
        COUNT=0
    fi
done
$target $@

