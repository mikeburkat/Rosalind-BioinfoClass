'''
Created on Dec 7, 2013

@author: Mike
'''

class OverlapGraph:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.Dna = []
        self.dataSet = "dataset_52_7.txt"
        self.testSet = "overlap_graph_1.txt"
    
    
    def overlap(self, dna):
        over = []
        
        for suffix in dna:
            suf = suffix[1:]
            for prefix in dna:
                pre = prefix[:-1]
                if pre == suf:
                    over.append(suffix + " -> " + prefix)
        
        over.sort(cmp=None, key=None, reverse=False)
        return over
    
    
    def read(self, f):
        lines = f.readlines()
        
        for l in lines:
            if l == "Output:\n":
                break
            self.Dna.append(l.rstrip('\n'))
        
        #self.k = 5
        #self.Dna = 'CAATCCAAC'
            
    def printVAR(self):
        s = ''
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
        result = self.overlap(self.Dna)
        for r in result:
            print r
        
def getFile(fileName):
    from os.path import expanduser
    home = expanduser("~")
    path = home + '//Downloads//' + fileName 
    #print path
    fileToOpen = open(path , 'r')
    return fileToOpen
       
if __name__ == '__main__':
    og = OverlapGraph()
    #test = True
    test = False
    f = getFile(og.getFileName(test))    
    if test:
        f.readline()
    
    og.autoRun(f)       