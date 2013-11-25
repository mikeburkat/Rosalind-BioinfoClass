'''
Created on Nov 24, 2013

@author: Mike
'''
from MotifEnumeration import *


def getFile(fileName):
    from os.path import expanduser
    home = expanduser("~")
    path = home + '//Downloads//' + fileName 
    #print path
    fileToOpen = open(path , 'r')
    return fileToOpen


if __name__ == '__main__':
    motifEnum = MotifEnumeration()
    test = True
    f = getFile(motifEnum.getFileName(test))    
    if test:
        f.readline()
    
    
    motifEnum.read(f)
    print motifEnum.printVAR()