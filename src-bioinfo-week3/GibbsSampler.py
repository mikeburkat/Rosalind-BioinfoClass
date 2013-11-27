'''
Created on Nov 27, 2013

@author: Mike
'''

class GibbsSampler:
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
        self.dataSet = "dataset_43_4.txt"
        self.testSet = "gibbs_sampler.txt"
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


    def motifBasedOnProbabilities(self, kmers, profile):
        import random
        probDic = {}
        sum = 0
        #print self.order
        #for p in profile:
            #print p
        for kmer in kmers:
            prob = 1
            for x in range(len(kmer)):
                for y in range(len(self.order)):
                    if kmer[x] == self.order[y]:
                        prob = prob * profile[x][y]
            probDic[kmer] = prob
            sum += prob
    
        #print probDic
        #print "sum:", sum
        
        sumAdj = 0
        for p in probDic:
            probDic[p] = probDic[p] / sum
            sumAdj += probDic[p]
        #print probDic
        #print "sum:", sumAdj
        
        
        prev = 0
        for p in probDic:
            probDic[p] = probDic[p] + prev
            prev = probDic[p]
        
        last = probDic.keys()[-1] 
        probDic[last] = 1.0
        #print probDic
        
        
        i = random.uniform(0, 1)
        #print i
        probabilityChosenKmer = ''
        #print probDic
        for p in probDic:
            if probDic[p] >= i:
                probabilityChosenKmer = p
                break
            
        
        
        return probabilityChosenKmer
        
    
    def motif(self, kmers, consensus):
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
                        if len(Hz) != 15:
                            print len(Hz)
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
        import random
        bestMotifs = list(self.randomKmers)
        motifs = self.randomKmers
        #print "new run"
        for x in range(self.n):
            i = random.randrange(self.t)
            #print i
            #print motifs, self.score(motifs)
            
            motifs.pop(i)
            profile = self.profile(motifs)
            consensus = self.getConsensus(profile)
            #print profile
            motifs.insert(i, (self.motifBasedOnProbabilities(self.DNAkmers[i], profile)) )
                
            #print motifs, self.score(motifs)
            if self.score(motifs) < self.score(bestMotifs):
                bestMotifs = list(motifs)
                #print "again"
                
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
        self.n = int(params[2])
        
        lines = f.readlines()
        
        for l in lines:
            if l == "Output\n":
                break
            self.Dna.append(l.rstrip('\n'))
        
            
    def printVAR(self):
        s = ''
        s += "k: " + str(self.k) + "\n"
        s += "t: " + str(self.t) + "\n"
        s += "n: " + str(self.n) + "\n"
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
        
        x = 0
        results = []
        while x in range(20):
            self.selectRandom()
            t = self.searchForBest()
            results.append( t )
            print "Best from round", x, t, self.score(t)
            x += 1
            
        #x = self.mostFrequent(results)
        x = self.findBest(results)
        #print self.score(x)
        
        s = ''
        s += str(self.score(x)) + "\n"
        for i in x:
            s += i + "\n"
        print s
        return s
        
def getFile(fileName):
    from os.path import expanduser
    home = expanduser("~")
    path = home + '//Downloads//' + fileName 
    #print path
    fileToOpen = open(path , 'r')
    return fileToOpen
       
if __name__ == '__main__':
    gs = GibbsSampler()
    test = False
    f = getFile(gs.getFileName(test))    
    if test:
        f.readline()
    
    gs.autoRun(f)
    
    
    
    