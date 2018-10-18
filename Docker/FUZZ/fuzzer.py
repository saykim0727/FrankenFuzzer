import subprocess
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
		rm = subprocess.Popen(['rm','-rf','/FUZZ/share/core/*'])	
		rm.wait()
		rm = subprocess.Popen(['rm','-f','/FUZZ/share/log/*'])	
		rm.wait()
		os.system("mkdir /FUZZ/share/core/%s" % (self.fuzz))
		while True:
			if self.fuzz=="afl-fuzz":
				afl = AFL(self.dumb,self.indir,self.outdir,self.target,self.type)
			elif self.fuzz=="radamsa":
				radamsa = RADAMSA(self.indir,self.outdir,self.target)
			elif self.fuzz=="honggfuzz":
				honggfuzz = HONGGFUZZ(self.indir,self.outdir,self.target)
			elif self.fuzz=="hodor":
				hodor = HODOR(self.indir,self.outdir,self.target)
			else:
				printf("Unknown fuzzer")

class AFL:
	path = "/FUZZ/mod/afl/afl-fuzz"
	def __init__(self, dumb,indir,outdir,target,t):	
		self.run(dumb,indir,outdir,target,t)
	
	def run(self, dumb,indir,outdir,target,t):	
		cmd = ""
		if dumb=="False":
			cmd = "%s -i %s -o %s %s" % (self.path,indir,outdir,target)
		else:
			cmd = "%s -i %s -o %s -Q %s" % (self.path,indir,outdir,target)	
		if t=="True": #file
			cmd = cmd + " @@"
		AFL_proc = subprocess.call(cmd,shell=True)

class RADAMSA:
	path = "/FUZZ/mod/radamsa"
	def __init__(self,indir,outdir,target):	
		run(indir,outdir,target)
	
	def run(self,indir,outdir,target):
		file_list = os.listdir(indir)
		cmd = "cat %s | %s -o %s" % (indi+"/"+file_list[0], self.path,"/FUZZ/mod/radamsa.seed")
		radamsa_proc = subprocess.call(cmd,shell=True)
		radamsa.wait()
		cmd = "%s < %s" %(target, "/FUZZ/mod/radamsa.ssed")
		radamsa_proc = subprocess.call(cmd,shell=True)

class HODOR:
	def __init__(self,indir,outdir,target):
		self.run(indir,outdir,target)
	
	def run(self,indir,outdir,target):
		pass	

class HONGGFUZZ:
	path = "/FUZZ/mod/honggfuzz/honggfuzz"
	def __init__(self,indir,outdir,target):	
		self.run(indir,outdir,target)

	def run(self,indir,outdir,target):
		cmd = "%s -n1 -u -f %s -W %s -- %s ___FILE___" % (self.path,indir,outdir,target)
		hong_proc = subprocess.call(cmd,shell=True)	
		
class CoreMonitor(): #for radamsa, hodor
	def __init__(self,fuzzer,dumb):	
		pass


if  __name__== "__main__":
	argv=[]
	for i in sys.argv:
		argv.append(i)
	while True:	
		fuzzer = Fuzzer(argv)
		fuzzer.runFuzzer()
