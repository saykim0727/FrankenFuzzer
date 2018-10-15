from fuzzer import * 
import os
import sys
import argparse
import time

class Main:
	fuzz_list = ["afl-fuzz","radamsa","honggfuzz","hodor"]
	def __init__(self):
		parser = argparse.ArgumentParser(description='FrankenFuzzer')
		parser.add_argument('-i', type=str, default="/FUZZ/Seed",help='an integer for the accumulator')
		parser.add_argument('-o', type=str, default="/FUZZ/share/core",help='an integer for the accumulator')
		parser.add_argument('-d', type=str, default="False", help='an integer for the accumulator')
		parser.add_argument('t',type=str,help="aaa")
		#for honggfuzz, afl
		#parser.add_argument('-t', type=int, default=10, help='an integer for the accumulator')
		#for honggfuzz, afl
		self.args = parser.parse_args()

	def run(self):
		for i in self.fuzz_list: 
			docker = Docker()
			docker.runDocker(self.args,i)
		time.sleep(1) #time for running all fuzzer

		
class Docker:

	def __init__(self):
		pass

	def runDocker(self,args,fuzzer):
		os.chdir("../")
		subprocess.call("./run_docker.sh f-%s %s %s %s %s/%s %s" % (fuzzer, fuzzer,args.d,args.i,args.o,fuzzer,args.t),shell=True)
		os.chdir("./FUZZ")


class Monitor:
	def __init__(self):
		self.indir = ConfigParsor("MONITOR_IN")
		self.outdir = ConfigParsor("MONITOR_OUT")

	
			

if __name__ == "__main__":
	main = Main()
	main.run()
	
