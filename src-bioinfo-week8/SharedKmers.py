'''
Created on Feb 20, 2014

@author: mike
'''

class SharedKmers():


    def __init__(self):
        self.k = 3
        self.g = "AAACTCATC"
        self.h = "TTTCAAATC"
        self.dataSet = "dataset_91_2 (4).txt"
        
    def reverseComplement(self, sequence):
        revCompS = ''
        for c in sequence:
            if c == 'A':
                revCompS = 'T' + revCompS
            if c == 'T':
                revCompS = 'A' + revCompS
            if c == 'C':
                revCompS = 'G' + revCompS
            if c == 'G':
                revCompS = 'C' + revCompS
            if c == 'N':
                revCompS = c + revCompS
        return revCompS
        

    def getKmers(self, k, g):
        kmers = {}
        i = 0
        while ( i <= len(g) - k):
            kmer = g[i:i+k]
            
            if kmer in kmers:
                kmers[kmer].append(i)
            else:
                kmers[kmer] = [i]
            
            i += 1
        return kmers
    
    def findShared(self, g, h):
        shared = []
        
        
        for k in g.keys():
            allNew = []
            
            if k in h:
                gI = g[k]
                hI = h[k]
                
                for x in gI:
                    for y in hI:
                        if (x, y) not in shared:
                            shared.append((x, y))
                        
            
            r = self.reverseComplement(k)
            if r in h:
                gI = g[k]
                hI = h[r]
                
                for x in gI:
                    for y in hI:
                        if (x, y) not in shared:
                            shared.append((x, y))
                        
        return shared
    
    
    def nicePrint(self, shared):
        for s in shared:
            print s
    
    def getFileName(self, test):
        if test:
            return self.testSet
        else:
            return self.dataSet
    
    def read(self, f):
         
        k = int( f.readline() )
        g = f.readline().rstrip('\n')
        h = f.readline().rstrip('\n')
        
        print len(g)
        print len(h)
        
        self.k = k
        self.g = g
        self.h = h
        
        f.readline()
    
    def run(self, f):
        
        self.read(f)
        
        gKmers = self.getKmers(self.k, self.g)
        #print gKmers
        hKmers = self.getKmers(self.k, self.h)
        #print hKmers
        
        shared = self.findShared(gKmers, hKmers)
        
        self.nicePrint(shared)



def getFile(fileName):
    from os.path import expanduser
    home = expanduser("~")
    
    path = home + '/Downloads/' + fileName 
    #print path
    fileToOpen = open(path , 'r')
    return fileToOpen

if __name__ == '__main__':
    sk = SharedKmers()
    
    test = True
    test = False
    f = getFile(sk.getFileName(test))    
    if test:
        f.readline()
    
    sk.run(f)