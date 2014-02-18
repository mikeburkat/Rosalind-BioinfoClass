'''
Created on Dec 7, 2013

@author: Mike
'''

class StringComposition:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.k = 0
        self.Dna = ''
        self.dataSet = "dataset_51_3 (1).txt"
        self.testSet = "string_com.txt"
        
        
    def composition(self, dna, k):
        comp = []
        x = 0
        while x+k <= len(dna):
            comp.append(dna[x:x+k])
            x += 1
        
        comp.sort(cmp=None, key=None, reverse=False)   
        return comp
     
    def read(self, f):
        k = f.readline()
        self.k = int(k)
        l = f.readline()
        self.Dna = (l.rstrip('\n'))
        
        #self.k = 5
        #self.Dna = 'CAATCCAAC'
            
    def printVAR(self):
        s = ''
        s += "k: " + str(self.k) + "\n"
        s += "DNA: " + self.Dna
        return s

    def getFileName(self, test):
        if test:
            return self.testSet
        else:
            return self.dataSet


    def autoRun(self, f):
        self.read(f)
        #print self.printVAR()
        result = self.composition(self.Dna, self.k)
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
    sc = StringComposition()
    #test = True
    test = False
    f = getFile(sc.getFileName(test))    
    if test:
        f.readline()
    
    sc.autoRun(f)       