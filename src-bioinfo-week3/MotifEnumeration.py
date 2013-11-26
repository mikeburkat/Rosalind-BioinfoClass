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
        self.dataSet = "dataset_36_7.txt"
        self.testSet = "motif_enumeration_data.txt"
        self.kmers = []
        
        
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
    
    
    def allKmers(self, kmer, length):
        if length == 0:
            self.kmers.append(kmer)
            return
        
        for x in ['A', 'C', 'G', 'T']:
            self.allKmers(kmer + x, length - 1)
        
            
    def getKmers(self):
        return self.kmers
    

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
            
    def hammingDistance(self, a, b):
        distance = 0
        
        for c1, c2 in zip(a, b):
            if c1 != c2:
                distance += 1
        
        return distance
        
        
    def findAllKmers(self):
        matches = ""
        for km in self.kmers:
            isInAllDNA = 0
            
            for dna in self.Dna:
                x = 0
                found = False
                while x + self.k <= len(dna):
                    if self.hammingDistance(km, dna[x : x + self.k]) <= self.d :
                        isInAllDNA += 1
                        found = True
                        break
                    x += 1
                
                if not found:
                    break
                    
            if isInAllDNA == len(self.Dna):
                matches += km + " "
                
        return matches
            
    
    
    def autoRun(self, f):
        self.read(f)
        #print self.printVAR()
        self.allKmers("", self.k)
        #print self.getKmers()
        print self.findAllKmers()
        
        
        
        
def getFile(fileName):
    from os.path import expanduser
    home = expanduser("~")
    path = home + '//Downloads//' + fileName 
    #print path
    fileToOpen = open(path , 'r')
    return fileToOpen
       
if __name__ == '__main__':
    motifEnum = MotifEnumeration()
    test = False
    f = getFile(motifEnum.getFileName(test))    
    if test:
        f.readline()
    
    motifEnum.autoRun(f)
    
    