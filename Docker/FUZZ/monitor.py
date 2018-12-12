from fuzzer import *
import sys
import uuid

class CoreMonitor(): #for crash monitor
    def __init__(self,seed,fuzzer):
        import shutil
        from shutil import move
        for filename in os.listdir("/TEMP"):
            randomString = uuid.uuid4()
            move("/TEMP/%s" % (filename),"/FUZZ/share/core_file/%s" %(filename))
            shutil.copyfile(seed,"/FUZZ/share/core/"+fuzzer+"/"+fuzzer+"-"+str(randomString))
#            shutil.copyfile(seed,"/FUZZ/share/seed/"+fuzzer+"-"+str(randomString))

if __name__ == "__main__":
    fuzzer = ""
    with open("/tmp/fuzzer","r") as f:
        fuzzer = f.readline()[:-1]
    monitor = CoreMonitor(sys.argv[2],fuzzer)
