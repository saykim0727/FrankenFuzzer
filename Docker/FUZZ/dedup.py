from pwn import process
import glob
import sys
import os

if len(sys.argv) < 3 :
    print("[!] USAGE : python ./dedup.py [target] [crash dir path]")
    sys.exit()

crashList = []
dirList = glob.glob("%s%s"%(sys.argv[2], "/*"))
target = sys.argv[1]

for fileName in dirList :
    if fileName.find("core") > 0:
        coreDump = fileName

        gdbCmd = ["sudo","gdb", "-q", "-e", target, "-c", coreDump]
        p = process(gdbCmd)
        p.recvuntil("\n(gdb) ")
        p.sendline("bt")
        callStack = ""
        while(1):
            callStack += p.recv(10000)
            if callStack.find("\n(gdb)") >= 1 :
                break
            p.sendline("\r\n")
        p.kill()

        callStackList = callStack.split("#")[1:]
        line0 = callStackList[0]
        nbOfLines = len(callStackList)
        print(line0)
        newCrash = True
        for crash in crashList:
            if crash[1] == line0 and crash[2] == nbOfLines:
                os.remove(coreDump)
                newCrash = False
                break
        if newCrash:
            crashList.append([coreDump, line0, nbOfLines])
