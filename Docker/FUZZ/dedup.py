import pwn import process
import glob
import sys
import os

CHAR_LENGTH = 100

if len(sys.argv) < 3 or os.getuid() !=0 :
    print "[!] USAGE : python ./dna.py [ crash dir path ] [gdb or gdb-peda]"
    sys.exit()

coreDump = "" 
seedDir = ""
dirList = glob.glob("%s%s"%(sys.argv[1], "/*"))
debugger = sys.argv[2]
if debugger == "gdb":
    debugger = "(gdb)"

for fileName in dirList :
    if fileName.find("core") > 0 :
        coreDump = fileName
    else:
        seedDir  = fileName

#print "[!] coreDump = %s " %(coreDump)
#print "[!] seeDir = %s " %(seedDir)

crashType   = coreDump.split(".")[-1]
crashFile   = "../EOS/" + str(coreDump.split(".")[-3])
gdbCmd = ["gdb","-q",crashFile,"-c",coreDump]
print " ".join(gdbCmd)
p = process(gdbCmd,level='critical')

p.recvuntil(debugger)
p.sendline("bt")
callStack =""
while 1:
    callStack += p.recv(1000000)
    if(callStack.find("main()") >=0 or callStack.find(debugger)>=0):
        break;
    p.sendline("\r\n")

callStack += p.recvuntil(debugger)
callStackList = callStack.split("#")
for data in callStackList:
    strData = (data[0:CHAR_LENGTH]+"...." + data[-CHAR_LENGTH:-1]).split("\n")[0]
    print strData



print "[!] crashType = %s " %(crashType)
print "[!] crashFile = %s " %(crashFile)

