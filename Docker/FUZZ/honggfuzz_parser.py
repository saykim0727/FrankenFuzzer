import os


class CrushParser:
    argList = [0, 2, 4, 6, 8, 10]

    def __init__(self):
        self.crashList = []
        self.deleted = 0

    def run(self):
        with open("../share/log/honggfuzz.log", "r") as f:	#not sure about the path...
            for line in f:

# Lines that report crashes are structured this way:
# Crash: saved as 'path/to/file/crashfile'
                if line.split(' ')[0] == "Crash:":
                    crashName = line.split(' ')[3][1:-2]

# honggfuzz crashes look like this:
# path/to/crash/SIGSEGV.PC.7ffff7a828f0.STACK.c2e85b1e.CODE.128.ADDR.(nil).INSTR.mov____(%rdi),%edx.2018-10-18.18:05:42.128.fuzz
# so we split them on "." and use argList to index the useful data in the created list
                    self.find(crashName.split('.'))

    def find(self, crash):
        for cr in self.crashList:
            for index in self.argList:
                if crash[index] != cr[index]: # it means the new crash is different than cr
                    break
            self.delete(crash)  # if not, the crash is not new. We delete the crash file
            return
        self.crashList.append(crash)    # if we haven't found the crash in the list, we add it

    def delete(self, crash):
        self.deleted += 1
        os.remove(".".join(crash))	# not sure about the path...


parser = CrushParser()
parser.run()
print("deleted files %d" % parser.deleted)
print("Crashes saved:")
for c in parser.crashList:
    print(".".join(c))
