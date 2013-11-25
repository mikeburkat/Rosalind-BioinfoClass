'''
Created on Nov 24, 2013

@author: Mike
'''

class MotifEnumeration:
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.Dna = []
        self.k = 0
        self.d = 0
        self.dataSet = ""
        self.testSet = "motif_enumeration_data.txt"
        
        
    def set(self, Dna, k, d):
        self.Dna = Dna
        self.k = k
        self.d = d
        
    def printVAR(self):
        s = ''
        s += "d: " + str(self.d) + "\n"
        s += "k: " + str(self.k) + "\n"
        s += "DNA List:" + "\n"
        for d in self.Dna:
            s += d + "\n"
        return s
    
    def getFileName(self, test):
        if test:
            return self.testSet
        else:
            return self.dataSet
    
    

    def read(self, f):
        params = f.readline()
        params = params.rsplit()
        self.k = int(params[0])
        self.d = int(params[1])
        lines = f.readlines()
        
        for l in lines:
            if l == "Output\n":
                break
            self.Dna.append(l.rstrip('\n'))
            
        
    