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
		self.outdir = argv[4]
		self.target = self.target +  argv[5]

	def runFuzzer(self):	
		if self.fuzz=="afl-fuzz":
			afl = AFL(self.dumb,self.indir,self.outdir,self.target)
		elif self.fuzz=="radamsa":
			cmd = "cat %s | %s -o %s" % (self.args.i+file_list[random.randrange(0,len(file_list))], fuzz_path+fuzz_name,"./Seed/input")
		elif self.fuzz=="honggfuzz":
			pass
		elif self.fuzz=="hodor":
			pass
		else:
			printf("Unknown fuzzer");

class AFL:
	path = "/FUZZ/mod/afl/afl-fuzz"
	def __init__(self, dumb,indir,outdir,target):	
		self.run(dumb,indir,outdir,target)
	
	def run(self, dumb,indir,outdir,target):	
		cmd = ""
		if dumb=="False":
			cmd = "%s -i %s -o %s %s" % (self.path,indir,outdir,target)	
		else:
			cmd = "%s -i %s -o %s -Q %s" % (self.path,indir,outdir,target)	
		print cmd
		AFL_proc = subprocess.call(cmd,shell=True)
		AFL_proc.wait()

class RADAMSA:
	def __init__(self,fuzzer,dumb):	
		pass

class hodor:
	def __init__(self,fuzzer,dumb):	
		pass

class honggfuzz:
	def __init__(self,fuzzer,dumb):	
		pass
		
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
