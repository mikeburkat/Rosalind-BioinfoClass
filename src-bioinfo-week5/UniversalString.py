'''
Created on Dec 13, 2013

@author: Mike
'''

class UniversalString:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.dataSet = "dataset_57_5 (1).txt"
        self.testSet = "uni_str.txt"
        self.kMers = []
        self.k = 0
    
    def printResult(self, r):
        
        s = ''
        s += r[0]
        x = 1
        while x < len(r):
            
            s += r[x][-1:]
            x += 1
        
        print s
        
        
        
        
        
    def DeBrujinCycle(self, k):
        patterns = {}
        x = 0
        s = '0' * k
        end = 2 ** k
        patterns[s] = 0
        
        while len(s) < end:
            x += 1
            if s[x:]+'1' not in patterns:
                s += '1'
                patterns[s[x:]] = 0
                
            else:
                s += '0'
                patterns[s[x:]] = 0
                
        #print len(patterns)    
        #print patterns
        #print end
        #print len(s)
        
        return s
        
        
        
        
    
    def UniGen(self, kmer, k):
        
        if k == 0:
            self.kMers.append(kmer)
            return
        else:
            self.UniGen(kmer + "0", k - 1)
            self.UniGen(kmer + "1", k - 1)
        
        
            
    def read(self, f):
        k = f.readline()
        self.k = int(k)
        self.k = 18
        
        
    def printVAR(self):
        s = ''
        s += "k: " + str(self.k)
        return s

    def getFileName(self, test):
        if test:
            return self.testSet
        else:
            return self.dataSet

    def autoRun(self, f):
        self.read(f)
        #print self.printVAR()
        #self.UniGen("", self.k)
        #print self.kMers
        print self.DeBrujinCycle(self.k)
        
        
def getFile(fileName):
    from os.path import expanduser
    home = expanduser("~")
    path = home + '//Downloads//' + fileName 
    #print path
    fileToOpen = open(path , 'r')
    return fileToOpen
       
if __name__ == '__main__':
    us = UniversalString()
    test = True
    #test = False
    f = getFile(us.getFileName(test))    
    if test:
        f.readline()
    
    us.autoRun(f)    

