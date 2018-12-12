import subprocess
from monitor import *
from configParsor import ConfigParsor 
import os
import time
import random
import argparse
import sys

class Fuzzer:
    target = "/FUZZ/"
    def __init__(self,argv):    
        self.fuzz = argv[1]
        self.dumb = argv[2]
        self.indir = argv[3]
        self.outdir = argv[4] + "/" + self.fuzz
        self.type = argv[5]
        self.target = self.target +  argv[6]

    def runFuzzer(self):
        os.system("mkdir /FUZZ/share/core/%s" % (self.fuzz))
        while True:
            if self.fuzz=="afl-fuzz":
                afl = AFL(self.dumb,self.indir,self.outdir,self.target,self.type)
            elif self.fuzz=="radamsa":
                radamsa = RADAMSA(self.indir,self.outdir,self.target,self.fuzz,self.type)
            elif self.fuzz=="honggfuzz":
                honggfuzz = HONGGFUZZ(self.indir,self.outdir,self.target,self.type)
            else:
                printf("Unknown fuzzer")

class AFL:
    path = "/FUZZ/mod/afl/afl-fuzz"
    gcc_path = "/FUZZ/mod/afl/afl-gcc"
    def __init__(self, dumb,indir,outdir,target,t):    
        '''
        if dumb=="False":
            cmd = "%s -fno-stack-protector -o %s %s" %(self.gcc_path,target,target+".c")
            afl_gcc = subprocess(cmd,shell=True)
        '''
        self.run(dumb,indir,outdir,target,t)
    
    def run(self, dumb,indir,outdir,target,t):    
        cmd = ""
        if dumb=="False":
            cmd = "%s -i %s -o %s %s" % (self.path,indir,outdir,target)
        else:
            cmd = "%s -i %s -o %s -Q %s" % (self.path,indir,outdir,target)    
        if t=="True": #file
            cmd = cmd + " @@"
        AFL_proc = subprocess.Popen(cmd,shell=True)
        # run monitor module to run a target with afl_result for core dump
        AFL_proc.wait()
        # if afl is terminated, remove seed because the seed cause crash

    # for afl-gcc with source code
    def compile(self):
        pass

class RADAMSA:
    path = "/FUZZ/mod/radamsa"
    def __init__(self,indir,outdir,target,radamsa,_type):    
        self.run(indir,outdir,target,radamsa,_type)
    
    def run(self,indir,outdir,target,radamsa,_type):
        os.system("echo /TEMP/core.radamsa.%e.%p.%s > /proc/sys/kernel/core_pattern")
        file_list = os.listdir(indir)
        seed_name = "radamsa." + str(time.time())
        cmd = "cat %s | %s -o %s" % (indir+"/"+file_list[0], self.path,"/tmp/testcase")
        radamsa_proc = subprocess.Popen(cmd,shell=True)
        radamsa_proc.wait()
         
        if _type=="False":
            cmd = "%s < %s" %(target, "/tmp/testcase")
        else:
            cmd = "%s %s" %(target, "/tmp/testcase")
        radamsa_proc = subprocess.Popen(cmd,shell=True)
        radamsa_proc.wait()
        
class HONGGFUZZ:
    path = "/FUZZ/mod/honggfuzz/honggfuzz"
    def __init__(self,indir,outdir,target,_type):    
        self.run(indir,outdir,target,_type)

    def run(self,indir,outdir,target,_type):
        cmd=""
        if _type=="False":
            cmd = "%s -n1 -u -f %s -W %s -s -- %s" % (self.path,indir,outdir,target)
        else:
            cmd = "%s -n1 -u -f %s -W %s -- %s ___FILE___" % (self.path,indir,outdir,target)
        hong_proc = subprocess.Popen(cmd,shell=True)    
        #os.system("rm /FUZZ/share/seed/00000000000000000000000000000000.00000001.honggfuzz.cov")
        hong_proc.wait()

if  __name__== "__main__":
    argv=[]
    for i in sys.argv:
        argv.append(i)
    while True:    
        fuzzer = Fuzzer(argv)
        fuzzer.runFuzzer()
