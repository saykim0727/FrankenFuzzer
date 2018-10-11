from fuzzer import * 
import os
import sys
import argparse
import time

class Main:
	fuzz_list = ["afl-fuzz","radamsa","honggfuzz","hodor"]
	def __init__(self):
		parser = argparse.ArgumentParser(description='FrankenFuzzer')
		parser.add_argument('-i', type=str, default="./Seed",help='an integer for the accumulator')
		parser.add_argument('-o', type=str, default="./Output",help='an integer for the accumulator')
		parser.add_argument('-d', type=bool, default=False, help='an integer for the accumulator')
		parser.add_argument('-t', type=int, default=10, help='an integer for the accumulator')
		self.args = parser.parse_args()

	def run(self):
		for i in self.fuzz_list: 
			docker = Docker()
			docker.runDocker(self.args,i)
		time.sleep(10)
		
class Docker:

	def __init__(self):
		pass

	def runDocker(self,args,fuzzer):
		os.chdir("../")
		subprocess.call("./run_docker.sh f-%s" % (fuzzer),shell=True)
		os.chdir("./FUZZ")
			

if __name__ == "__main__":
	main = Main()
	main.run()

