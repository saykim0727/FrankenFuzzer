#!/bin/sh
if [ $1 = "afl-fuzz" ]
then
    echo "/FUZZ/share/core_file/core.$1.%e.%p.%s" > /proc/sys/kernel/core_pattern
	cd /FUZZ/mod/afl/qemu_mode
	./build_qemu_support.sh
	cd /
fi

if [ $1 = "honggfuzz" ]
then
    echo "/FUZZ/share/core_file/core.$1.%e.%p.%s" > /proc/sys/kernel/core_pattern
	wget https://github.com/google/honggfuzz/archive/1.7.tar.gz -O /FUZZ/mod/honggfuzz.tar.gz
	tar -xf /FUZZ/mod/honggfuzz.tar.gz -C /FUZZ/mod/
	mv /FUZZ/mod/honggfuzz-1.7 /FUZZ/mod/honggfuzz
	cd /FUZZ/mod/honggfuzz
	make
	cd /
fi
if [ $1 = "radamsa" ]
then
	mkdir /TEMP
	echo "/TEMP/core.$1.%e.%p.%s" > /proc/sys/kernel/core_pattern
fi

#service cron restart
/FUZZ/start.sh $1 $2 $3 $4 $5 $6  > /FUZZ/share/log/$1.log 2>&1 &
/bin/bash 
