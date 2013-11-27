'''
Created on Nov 26, 2013

@author: Mike
'''
import math
class GreedyMotifSearchPseudocounts:
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
        self.dataSet = "dataset_40_9.txt"
        #self.testSet = "greedy_data.txt"
        self.testSet = "greedy_pseudo.txt"
        self.bestProfile = []
        self.DNAkmers = []
        self.order = ['A', 'C', 'G', 'T']

    
    def hammingDistance(self, a, b):
        distance = 0
        for c1, c2 in zip(a, b):
            if c1 != c2:
                distance += 1
        return distance
    
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
            
    
    def score(self, profile):
        testProfile = self.profile(profile)
        consensus = self.getConsensus(testProfile)
        score = 0
        for p in profile:
            score += self.hammingDistance(consensus, p)
        return score
        
    
    def scoreEntropy(self, profile):
        testProfile = self.profile(profile)
        entropy = 0
        for t in testProfile:
            for i in t:
                if i != 0:
                    entropy += i * math.log(i,2)
        return -entropy
    
    
    def findBestProfile(self):
        first = True
        
        for motif in self.DNAkmers[0]:
            profile = [motif]
            
            
            i = 1
            while i < self.t:
                testProfile = self.profile(profile)
                #print motif
                #print testProfile
                mostProbable = self.findMostProbable(self.DNAkmers[i], profile)
                profile.append(mostProbable)
                i += 1
                
            #print profile, self.score(profile)
            
            if first or self.score(profile) < self.score(self.bestProfile) :
                self.bestProfile = profile
                first = False
        
        return self.bestProfile
    
    
    def probability(self, kmer, profile):
        x = 0
        prob = 1
        while x < len(kmer):
            #print profile
            i = self.order.index(kmer[x])
            #print profile[x][i]
            if profile[x][i] != 0:
                prob = float(prob * float(profile[x][i]))
            x += 1
        return prob
    
    
    
    def findMostProbable(self, kmers, profile):
        #print profile
        mostProb = kmers[0]
        score = 0
        for p in profile:
            score += self.hammingDistance(mostProb, p)
        bestScore = score
        
        for k in kmers:
            score = 0
            for p in profile:
                score += self.hammingDistance(k, p)
                
            if score < bestScore:
                bestScore = score
                mostProb = k
        
        #print profile
        #print bestScore, mostProb
        
        return mostProb
    
    
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
        
        #self.k = 3
        #self.t = 5
        #self.Dna = []
        #self.Dna.append('GGCGTTCAGGCA')
        #self.Dna.append('AAGAATCAGTCA')
        #self.Dna.append('CAAGGAGTTCGC')
        #self.Dna.append('CACGTCAATCAC')
        #self.Dna.append('CAATAATATTCG')
            
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
        self.breakToKmers()
        #print self.findBestOfFirstTwo()
        x = self.findBestProfile()
        print len(x), x
        s = ''
        for i in x:
            s += i + "\n"
            
        print s
        #print self.profile(['AACTTC', 'AATCTT', 'ACTCAT', 'ACTCGG', 'AGTCGT'])
        
def getFile(fileName):
    from os.path import expanduser
    home = expanduser("~")
    path = home + '//Downloads//' + fileName 
    #print path
    fileToOpen = open(path , 'r')
    return fileToOpen
       
if __name__ == '__main__':
    gms = GreedyMotifSearchPseudocounts()
    test = False
    f = getFile(gms.getFileName(test))    
    if test:
        f.readline()
    
    gms.autoRun(f)