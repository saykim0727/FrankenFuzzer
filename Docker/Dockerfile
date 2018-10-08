FROM ubuntu:18.04
MAINTAINER F-fuzz <saykim0727@kaist.ac.kr>

RUN sed -i 's/security.ubuntu.com/ftp.daumkakao.com/g' /etc/apt/sources.list
RUN sed -i 's/archive.ubuntu.com/ftp.daumkakao.com/g' /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y vim
RUN apt-get install -y python
RUN apt-get install -y python-pip
RUN pip install --upgrade pip
RUN apt-get install -y gdb
RUN apt-get install -y strace
RUN apt-get install -y clang
RUN apt-get install -y openssh-server
RUN apt-get install -y net-tools
RUN pip install psutil

RUN apt-get install -y cron

RUN ulimit -c unlimited
CMD echo "/FUZZ/share/core/core.%e.%p.%s" > /proc/sys/kernel/core_pattern 
