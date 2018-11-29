#!/bin/bash
#./coverageTest.sh [FUZZ_NAME]
FUZZ=$1
SEED="./seed"
target="./target.sh"
if [ $FUZZ = "afl-fuzz" ]; then
    ./afl/afl-fuzz -i $SEED -o ./afl/output -- $target
elif [ $FUZZ = "honggfuzz" ]; then
    ./honggfuzz/honggfuzz -n1 -u -f $SEED -W ./honggfuzz/output -- $target
else
    while :
    do
        res_array=($(ls $SEED))
        ra_length=${#res_array[@]}
        INDEX=$(python -c 'import random; print random.randrange(0,'$ra_length');')
        FILE=${res_array[$INDEX]}
        cat $FILE | ./radamsa/radamsa -o ./radamsa/testcase
        $target < ./radamsa/testcase
    done
fi
