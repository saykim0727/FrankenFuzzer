import subprocess
from configParsor import ConfigParsor 
import os
import random

class Fuzzer:
	fuzz_list = ["afl-fuzz","radamsa","honggfuzz"]

	def __init__(self,args,fuzzer):
		self.args=args
	
	def runFuzzer(self,fuzz_name,fuzz_path):	
		file_list = os.listdir(self.args.i)
		if fuzz_name=="radamsa":
			cmd = "cat %s | %s -o %s" % (self.args.i+file_list[random.randrange(0,len(file_list))], fuzz_path+fuzz_name,"./Seed/input")

		os.chdir("../")
		print self.args.i
		subprocess.call("./run_docker.sh f-%s" %(fuzz_name),shell=True)		

if __name__ == "__main__":
	fuzzer = Fuzzer()
