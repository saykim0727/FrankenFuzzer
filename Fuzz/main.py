from fuzzer import * 
import os
import sys
import argparse

class Main:
	def __init__(self):
		parser = argparse.ArgumentParser(description='FrankenFuzzer')
		parser.add_argument('-i', type=str, default="../Docker/Seed",help='fuzzing seed directory',metavar="DIR")
		parser.add_argument('-o', type=str, default="../Docker/Output",help='fuzzing output directory',metavar="DIR")
		parser.add_argument('-d', action="store_true",default=False, help='dumb fuzzing')
		parser.add_argument('-t', type=int, default=10, help='timeout [10-500], default=10',metavar="[10-500]")
		parser.add_argument('target', type=str, help='fuzzing target file')
		self.args = parser.parse_args()

	def run(self):
		fuzzer = Fuzzer(self.args)
		
		
	
if __name__ == "__main__":
	fuzzer = Main()
	fuzzer.run()
