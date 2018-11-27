#!/bin/bash
/bin/ls
/bin/ps
cat "/asdf" | \
while read line
do
    echo $line
done

cat "./result" | \
while read line
do
    echo $line
done
