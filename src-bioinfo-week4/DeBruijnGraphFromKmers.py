'''
Created on Dec 7, 2013

@author: Mike
'''

class DeBruijnGraphFromKmers:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.Dna = []
        self.dataSet = "dataset_54_7.txt"
        self.testSet = "debruijn_graph_kmers.txt"
    
    
    def debruijn2(self, dna):
        import collections
        temp = {}
        
        x = 0
        while x < len(dna):
            y = 0
            suffix = dna[x][1:]
            while y < len(dna):
                prefix = dna[y][:-1]
                if prefix[:-1] == suffix[1:]:
                    #print suffix, prefix
                    if suffix in temp:
                        #if prefix not in temp[suffix]:
                        #    temp[suffix].append(prefix)
                        temp[suffix].append(prefix)
                    else:
                        temp[suffix] = [prefix]
                y += 1
            x += 1
        
        res = collections.OrderedDict(sorted(temp.items()))
        for r in res:
            print r, res[r]
        
        out = []
        return out
    
    
    def debruijn(self, dna):
        import collections
        temp = {}
        
        for d in dna:
            prefix = d[:-1]
            suffix = d[1:]
            if prefix in temp:
                temp[prefix].append(suffix)
            else:
                temp[prefix] = [suffix]
            
        res = collections.OrderedDict(sorted(temp.items()))
        output = []
        for r in res:
            output.append( r + " -> " + ','.join(res[r]) )
        
        return output
    
    
    
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
        result = self.debruijn(self.Dna)
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
    dbgfk = DeBruijnGraphFromKmers()
    #test = True
    test = False
    f = getFile(dbgfk.getFileName(test))    
    if test:
        f.readline()
    
    dbgfk.autoRun(f)    
        