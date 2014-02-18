'''
Created on Nov 25, 2013

@author: Mike
'''

class ProfileMostProbableKmer:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.Dna = ''
        self.k = 0
        self.dataSet = "dataset_39_3.txt"
        self.testSet = "profile_most_data.txt"
        self.kmers = []
        self.order = []
        self.profile = []



    def breakToKmers(self):
        x = 0
        while x + self.k <= len(self.Dna):
            self.kmers.append(self.Dna[x : x + self.k])
            x += 1
            
        return self.kmers
    
    def probability(self, kmer):
        x = 0
        prob = 1
        while x < len(kmer):
            i = self.order.index(kmer[x])
            #print self.profile[x][i]
            prob = prob * float(self.profile[x][i])
            
            x += 1
        return prob
        
    
    

    def findMostProbable(self):
        mostProb = self.kmers[0]
        probMostProb = self.probability(mostProb)
        
        for k in self.kmers:
            contender = self.probability(k)
            if contender > probMostProb:
                mostProb = k
                probMostProb = contender
        return mostProb



    def read(self, f):
        Dna = f.readline().rstrip('\n')
        self.Dna = Dna
        k = f.readline()
        self.k = int(k)
        order = f.readline()
        order = order.rstrip('\n')
        self.order = order.split()
        
        lines = f.readlines()
        
        profile = []
        for l in lines:
            if l == "Output\n":
                break
            profile.append(l.rstrip('\n'))
        for p in profile:
            self.profile.append(p.split())
            
    def printVAR(self):
        s = ''
        s += "k: " + str(self.k) + "\n"
        s += "DNA: " + self.Dna + "\n"
        s += str(self.order) + "\n"
        for p in self.profile:
            s += str(p) + "\n"
        
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
        print self.findMostProbable()
        

        
def getFile(fileName):
    from os.path import expanduser
    home = expanduser("~")
    path = home + '//Downloads//' + fileName 
    #print path
    fileToOpen = open(path , 'r')
    return fileToOpen
       
if __name__ == '__main__':
    pmpk = ProfileMostProbableKmer()
    test = False
    f = getFile(pmpk.getFileName(test))    
    if test:
        f.readline()
    
    pmpk.autoRun(f)