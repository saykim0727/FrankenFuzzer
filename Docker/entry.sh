#!/bin/sh
if [ $1 = "afl-fuzz" ]
then
	echo "core" > /proc/sys/kernel/core_pattern
else
	echo "/CORE/core.%e.%p.%s" > /proc/sys/kernel/core_pattern
fi
#service cron restart
/FUZZ/start.sh $1 $2 $3 $4 $5  > /FUZZ/share/log/$1.log 2>&1 &
/bin/bash 
