#!/bin/sh 
NAME="ffuzz"
DUMB="0"
FUZZ="afl-fuzz"
if [ $1 ]
then
	NAME=$1
fi
if [ $2 ]
then
	FUZZ=$2
fi
if [ $3 ]
then
	DUMB=$3
fi
sudo docker rm $NAME
sudo docker kill $NAME

sudo docker build --tag $NAME:1.0 ./

SHARED="-v `pwd`/share/:/FUZZ/share"
OPTION="--rm --privileged --cap-add=SYS_PTRACE --ulimit core=-1 --security-opt seccomp=unconfined"

sudo docker run -idt --name $NAME $PORT $SHARED $OPTION $NAME:1.0 /entry.sh $FUZZ $DUMB $4 $5 $6
#sudo docker run -idt --name $NAME $PORT $SHARED $OPTION $NAME:1.0 /bin/bash
