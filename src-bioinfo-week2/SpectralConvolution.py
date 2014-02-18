'''
Created on Nov 20, 2013

@author: mike
'''
import math

def findAllDiff(w):
    diff = []
    x = 0
    y = 0
    while x < len(w):
        y = x + 1
        while y < len(w):
            #print w[x], w[y], abs( w[x]- w[y] )
            diff.append(abs( w[x]- w[y] ))
            y += 1
        
        x += 1
    
    
    return diff


def splitSeqtoInt(seq):
    weightIntList = []
    for i in seq:
        weightIntList.append(int(i))
    
    return weightIntList
    

def getFile():
    from os.path import expanduser
    home = expanduser("~")
    #fileName = raw_input("File name: ")
    fileName = "spectral_convolution_data.txt"
    #fileName = "dataset_26_4.txt"
    #fileName = ""
    path = home + '/Downloads/' + fileName 
    # print path
    fileToOpen = open(path , 'r')
    return fileToOpen

if __name__ == '__main__':
    global allFragments 
    f = getFile()
    f.readline()
    listW = f.readline()
    #f.readline()
    #out = f.readline()
    #outS = out.split()
    #outL = splitSeqtoInt(outS)
    #outL.sort(cmp=None, key=None, reverse=False)
    
    weightList = listW.split()
    wL = splitSeqtoInt(weightList)
    
    
    adiff = findAllDiff(wL)
    adiff.sort(cmp=None, key=None, reverse=False)
    while 0 in adiff:
        adiff.remove(0)
    print adiff
    s = ''
    for i in adiff:
        s += str(i) + " "
    print s
   
    
    
    
    
    
    
    
    
    
    