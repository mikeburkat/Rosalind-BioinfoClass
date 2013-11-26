'''
Created on Nov 25, 2013

@author: Mike
'''

class MedianString:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.Dna = []
        self.k = 0
        self.dataSet = "dataset_38_7.txt"
        self.testSet = "medium_string_data.txt"
        self.DNAkmers = []
        self.kmers = []


    def read(self, f):
        k = f.readline()
        self.k = int(k)
        lines = f.readlines()
        
        for l in lines:
            if l == "Output\n":
                break
            self.Dna.append(l.rstrip('\n'))
            
            
    def breakToKmers(self):
        for dna in self.Dna:
            kmers = []
            x = 0
            while x + self.k <= len(dna):
                kmers.append(dna[x : x + self.k])
                x += 1
                
            self.DNAkmers.append(kmers)
        return self.DNAkmers

    def allKmers(self, kmer, length):
        if length == 0:
            self.kmers.append(kmer)
            return
        
        for x in ['A', 'C', 'G', 'T']:
            self.allKmers(kmer + x, length - 1)
                
    
    def hammingDistance(self, a, b):
        distance = 0
        
        for c1, c2 in zip(a, b):
            if c1 != c2:
                distance += 1
        
        return distance
    
    def d(self, pat):
        score = 0
        for kmers in self.DNAkmers:
            lowOfDNA = 200
            for k in kmers:
                hD = self.hammingDistance(k, pat)
                if hD < lowOfDNA :
                    lowOfDNA = hD
            score += lowOfDNA
        return score
    
    def findBestKmer(self):
        bestPat = ''
        score = 200
        for pattern in self.kmers:
            contender = self.d(pattern)
            if score >= contender:
                score = contender
                bestPat = pattern
        
        return bestPat
        
        
        
        
    def printVAR(self):
        s = ''
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


    def autoRun(self, f):
        self.read(f)
        #print self.printVAR()
        print self.breakToKmers()
        kmers = []
        self.allKmers("", self.k)
        print self.kmers
        print self.findBestKmer()
        

        
def getFile(fileName):
    from os.path import expanduser
    home = expanduser("~")
    path = home + '//Downloads//' + fileName 
    #print path
    fileToOpen = open(path , 'r')
    return fileToOpen
       
if __name__ == '__main__':
    ms = MedianString()
    test = False
    f = getFile(ms.getFileName(test))    
    if test:
        f.readline()
    
    ms.autoRun(f)
    
    
    
    
    
    
    
    
    
    
    
    
    
       