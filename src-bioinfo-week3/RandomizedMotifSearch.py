'''
Created on Nov 26, 2013

@author: Mike
'''

class RandomizedMotifSearch:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.Dna = []
        self.k = 0
        self.t = 0
        self.dataSet = "dataset_41_42.txt"
        self.testSet = "greedy_data.txt"
        self.bestProfile = []
        self.DNAkmers = []
        self.order = ['A', 'C', 'G', 'T']
        self.randomKmers = []
        
    def hammingDistance(self, a, b):
        distance = 0
        for c1, c2 in zip(a, b):
            if c1 != c2:
                distance += 1
        return distance
    
    def getConsensus(self, profile):
        consensus = ''
        for i in profile:
            x = 0
            while x < self.order:
                if max(i) == i[x]:
                    consensus += self.order[x]
                    break
                x += 1
        return consensus
    
    def score(self, motifs):
        testProfile = self.profile(motifs)
        consensus = self.getConsensus(testProfile)
        score = 0
        for p in motifs:
            score += self.hammingDistance(consensus, p)
        return score


    def motifs(self, kmers, consensus):
        mostProb = kmers[0]
        bestScore = self.hammingDistance(mostProb, consensus)
        
        for k in kmers:
            score = 0
            score += self.hammingDistance(k, consensus)
            if score < bestScore:
                bestScore = score
                mostProb = k
                
        #print profile
        #print bestScore, mostProb
        return mostProb
    
    def profile(self, testProfile):
        Hz = []
        for t in testProfile[0]:
            Hz.append([1, 1, 1, 1])
        
        #print Hz
        
        for kmer in testProfile:
            x = 0
            while x < len(kmer):
                y = 0
                while y < len(self.order):
                    if kmer[x] == self.order[y]:
                        Hz[x][y] += 1
                    y += 1
                x += 1
                
                
        x = 0
        while x < len(Hz):
            sum = 0
            for h in Hz[x]:
                sum += h
            y = 0
            while y < len(Hz[x]):
                Hz[x][y] = float(Hz[x][y]) / sum
                y += 1
            x += 1
        #print Hz
        return Hz
    
    
    def searchForBest(self):
        bestMotifs = self.randomKmers
        motifs = self.randomKmers
        done = False
        while not done:
            profile = self.profile(motifs)
            consensus = self.getConsensus(profile)
            motifs = []
            
            for k in self.DNAkmers:
                motifs.append(self.motifs(k, consensus))
                
            #print motifs, self.score(motifs)
            if self.score(motifs) < self.score(bestMotifs):
                bestMotifs = motifs
                #print "again"
            else:
                #print "done"
                done = True
        return bestMotifs   
    
    
    def findBest(self,results):
        bestResult = results[0]
        
        for r in results:
            if self.score(r) < self.score(bestResult):
                bestResult = r
        
        return bestResult
    
    def selectRandom(self):
        from random import choice
        self.randomKmers = []
        for k in self.DNAkmers:
            self.randomKmers.append(choice(k))
        return self.randomKmers
        

    def breakToKmers(self):
        for dna in self.Dna:
            kmers = []
            x = 0
            while x + self.k <= len(dna):
                kmers.append(dna[x : x + self.k])
                x += 1
                
            self.DNAkmers.append(kmers)
        return self.DNAkmers


    def read(self, f):
        params = f.readline()
        params = params.rstrip('\n')
        params = params.split()
        self.k = int(params[0])
        self.t = int(params[1])
        
        lines = f.readlines()
        
        for l in lines:
            if l == "Output\n":
                break
            self.Dna.append(l.rstrip('\n'))
        
        #self.k = 8
        #self.t = 5
        #self.Dna = []
        #self.Dna.append('CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA')
        #self.Dna.append('GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG')
        #self.Dna.append('TAGTACCGAGACCGAAAGAAGTATACAGGCGT')
        #self.Dna.append('TAGATCAAGTTTCAGGTGCACGTCGGTGAACC')
        #self.Dna.append('AATCCACCAGCTCCACGTGCAATGTTGGCCTA')
            
    def printVAR(self):
        s = ''
        s += "k: " + str(self.k) + "\n"
        s += "t: " + str(self.t) + "\n"
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
        print self.printVAR()
        print self.breakToKmers()
        
        x = 0
        results = []
        while x in range(1000):
            self.selectRandom()
            results.append( self.searchForBest() )
            x += 1
            
        #x = self.mostFrequent(results)
        x = self.findBest(results)
        print self.score(x)
        
        s = ''
        for i in x:
            s += i + "\n"
        print s
        
        
def getFile(fileName):
    from os.path import expanduser
    home = expanduser("~")
    path = home + '//Downloads//' + fileName 
    #print path
    fileToOpen = open(path , 'r')
    return fileToOpen
       
if __name__ == '__main__':
    rms = RandomizedMotifSearch()
    test = False
    f = getFile(rms.getFileName(test))    
    if test:
        f.readline()
    
    rms.autoRun(f)