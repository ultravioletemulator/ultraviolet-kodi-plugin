import ctypes
import subprocess

class PlatformProviderSpectrum:
    id=49
    name ="sinclair-zx-spectrum"

    specLib = ctypes.cdll.LoadLibrary('/usr/lib/libspectrum8.so')
    supportedExtensions= ['.z80','.tap', '.tzx', '.snap']

def __init__ (self):
    print ("initiating platform provider"+self.name)

    def searchRom (query):
        return ['1','2','3']

    def downloadRom (name):
        return "Zip file"

    def listFile (file):
        return ['rom1','rom2']

    def playRom (self, name):
        subprocess.call(["fuse", "-rom="+name])
        return 1

    def getSupprotedExtensions (self):
        return self.supportedExtensions



    def downloadArt (name):
        return "art"

    def downloadCover(name):
        return "cover"

    def downloadSummary():
        return "summary"




     #def main():
                # for i in range(10):
                # Note, this uses the Python 2 print
                #print "Random = %d" % my_test_lib.get_random(1, 10)
                #my_test_lib.get_random(1, 10)
      #  return None
