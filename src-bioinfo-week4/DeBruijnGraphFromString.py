'''
Created on Dec 7, 2013

@author: Mike
'''

class DeBruijnGraphFromString:
    '''
    classdocs
    '''



    def __init__(self):
        '''
        Constructor
        '''
        self.k = 0
        self.Dna = ''
        self.dataSet = "dataset_53_6.txt"
        self.testSet = "debruijn_graph_string.txt"
    
    
    def DeBruijn(self, k, dna):
        output = {}
        
        x = 0
        while x+k <= len(dna):
            kmer = dna[x:x+k]
            prefix = kmer[0:k-1]
            suffix = kmer[1:k]
            if prefix in output:
                output[prefix].append(suffix)
            else:
                output[prefix] = []
                output[prefix].append(suffix)
                
            x += 1
        
        return output
    
    
    def read(self, f):
        k = f.readline()
        self.k = int(k)
        l = f.readline()
        self.Dna = l.rstrip('\n')
        
        #self.k = 5
        #self.Dna = 'CAATCCAAC'
            
    def printVAR(self):
        s = ''
        s += "k: " + str(self.k) + "\n"
        s += "DNA List: " + self.Dna+ "\n"
        return s

    def getFileName(self, test):
        if test:
            return self.testSet
        else:
            return self.dataSet


    def autoRun(self, f):
        import collections
        self.read(f)
        #print self.printVAR()
        result = self.DeBruijn(self.k, self.Dna)
        res = collections.OrderedDict(sorted(result.items()))
        for r in res:
            print r, "->", ','.join(res[r]) 
        
def getFile(fileName):
    from os.path import expanduser
    home = expanduser("~")
    path = home + '//Downloads//' + fileName 
    #print path
    fileToOpen = open(path , 'r')
    return fileToOpen
       
if __name__ == '__main__':
    dbgfs = DeBruijnGraphFromString()
    #test = True
    test = False
    f = getFile(dbgfs.getFileName(test))    
    if test:
        f.readline()
    
    dbgfs.autoRun(f)       
        