#!/bin/sh 
NAME="ffuzz"
if [ $1 ]
then
	NAME=$1
fi
sudo docker rm $NAME
sudo docker kill $NAME


sudo docker build --tag $NAME:1.0 ./

SHARED="-v `pwd`/share/:/FUZZ/share"
OPTION="--rm --privileged --cap-add=SYS_PTRACE --ulimit core=-1 --security-opt seccomp=unconfined"

#sudo docker run -idt --name $NAME $PORT $SHARED $OPTION $NAME:1.0 /init.sh
sudo docker run -idt --name $NAME $PORT $SHARED $OPTION $NAME:1.0 /bin/bash
