'''
Created on Jan 15, 2014

@author: Mike
'''
from BLOSUM62 import BLOSUM62

class node:
    
    def __init__(self, left, down, weight):
        self.backtrack = ''
        self.weight = 0
        self.left = left
        self.down = down
        
    def __str__(self):
        s = str(self.weight)
        return s
    
    

class graph:
    
    def __init__(self, n, m):
        self.n = n
        self.m = m
        
        self.s1 = ''
        self.s2 = ''
        
        self.middle = [[None for _ in range( m + 1 ) ] for _ in range( n + 1 )]
        self.lower = [[None for _ in range( m + 1 ) ] for _ in range( n + 1 )]
        self.upper = [[None for _ in range( m + 1 ) ] for _ in range( n + 1 )]
        self.bmid = [[None for _ in range( m + 1 ) ] for _ in range( n + 1 )]
        self.blow = [[None for _ in range( m + 1 ) ] for _ in range( n + 1 )]
        self.bup = [[None for _ in range( m + 1 ) ] for _ in range( n + 1 )]
        
        self.bl = BLOSUM62()
        
    
        
        
    def printGraph(self, g, name):
        
        i = 0
        while i < len(g):
            j = 0
            
            header = name + '  '
            row = '\t'
            while j < len(g[0]):
                if i == 0:
                    header += g[i][j].down + '\t'
                
                if g[i][j].weight == float('-inf') and name == 'L':
                    row += str(g[i][j].weight)
                else:
                    row += str(g[i][j].weight) + '\t'
                j += 1
            if i == 0:
                print header
            print g[i][j-1].left
            print row
            
            i += 1
        print
    
    def generateGraphs(self, s1, s2):
        self.generateGraph(self.upper, s1, s2, 'U')
        self.generateGraph(self.middle, s1, s2, 'M')
        self.generateGraph(self.lower, s1, s2, 'L')
        
        
    
    def addNode(self, g, i, j, left, down):
        g[i][j] = node(left, down, 0)
    
    
    def generateGraph(self, g, s1, s2, name):
        self.s1 = s1
        self.s2 = s2
        
        i = 0
        while i < len(s1) + 1:
            j = 0
            while j < len(s2) + 1:
                
                if i == 0 and j == 0:
                    self.addNode(g, i, j, ' ', ' ')
                elif i == 0:
                    self.addNode(g, i, j, ' ', s2[j-1])
                elif j == 0:
                    self.addNode(g, i,j, s1[i-1], ' ')
                else:
                    self.addNode(g, i, j, s1[i-1], s2[j-1])
                
                j += 1
            i += 1
        
        #self.printGraph(g, name)
    
    def computeScores(self):
        u = self.upper
        m = self.middle
        l = self.lower
        
        i = 0
        j = 0
        while i < self.n + 1:
            u[i][j].weight = float('-inf')
            if i == 0:
                m[i][j].weight = 0
            elif i == 1:
                m[i][j].weight = -11
            else:
                m[i][j].weight = m[i-1][j].weight - 1
            i += 1
        
        
        i = 0
        j = 0
        while j < self.m + 1:
            l[i][j].weight = float('-inf')
            if j == 0:
                m[i][j].weight = 0
            elif j == 1:
                m[i][j].weight = -11
            else:
                m[i][j].weight = m[i][j-1].weight - 1
            j += 1
        
        #self.printGraph(u, 'U')
        #self.printGraph(l, 'L')
        #self.printGraph(m, 'M')
        
        
        i = 0
        while i < self.n + 1:
            j = 0
            while j < self.m + 1:
                if i == 0 and j == 0:
                    self.blow[i][j] = 'E'
                    self.bmid[i][j] = 'E'
                    self.bup[i][j] = 'E'
                elif j == 0:
                    
                    l[i][j].weight = max(l[i-1][j].weight - 1, m[i-1][j].weight - 11)
                    self.blow[i][j] = 'd'
                    self.bmid[i][j] = 'd'
                    
                elif i == 0:
                    
                    u[i][j].weight = max(u[i][j-1].weight - 1, m[i][j-1].weight - 11)
                    self.bup[i][j] = 'r'
                    self.bmid[i][j] = 'r'
                    
                else:
                    
                    l[i][j].weight = max(l[i-1][j].weight - 1, m[i-1][j].weight - 11)
                    if l[i][j].weight == m[i-1][j].weight - 11:
                        self.blow[i][j] = 'Md'
                    else:
                        self.blow[i][j] = 'd'
                    
                    
                    u[i][j].weight = max(u[i][j-1].weight - 1, m[i][j-1].weight - 11)
                    if u[i][j].weight == m[i][j-1].weight - 11:
                        self.bup[i][j] = 'Mr'
                    else:
                        self.bup[i][j] = 'r'
                
                    m[i][j].weight = max(l[i][j].weight, u[i][j].weight, m[i-1][j-1].weight + self.bl.getScore(m[i][j].down, m[i][j].left))
                    if m[i][j].weight == l[i][j].weight:
                        self.bmid[i][j] = 'L'
                    elif m[i][j].weight == u[i][j].weight:
                        self.bmid[i][j] = 'U'
                    else: 
                        self.bmid[i][j] = 'D'  
                    
                    
                j += 1
            i += 1
            
        #self.printGraph(u, 'U')
        #self.printGraph(l, 'L')
        #self.printGraph(m, 'M')
        '''
        for x in self.blow:
            print x
        print
        for x in self.bmid:
            print x
        print
        for x in self.bup:
            print x
        '''
        
    def align(self):
        
        b = self.bmid
        
        s1 = self.s1
        s2 = self.s2
        v = ''
        w = ''
        
        i = self.n
        j = self.m
        max = self.middle[i][j].weight
        
        
        while b[i][j] != 'E':
            #print i, j, b[i][j]
            if b[i][j] == 'D':
                v = s1[i-1] + v
                w = s2[j-1] + w
                i -= 1
                j -= 1
            elif b[i][j] == 'L':
                b = self.blow
            elif b[i][j] == 'U':
                b = self.bup
            elif b[i][j] == 'd':
                v = s1[i-1] + v
                w = '-' + w
                i -= 1
            elif b[i][j] == 'r':
                v = '-' + v
                w = s2[j-1] + w
                j -= 1
            elif b[i][j] == 'Mr':
                b = self.bmid
                v = '-' + v
                w = s2[j-1] + w
                j -= 1
            elif b[i][j] == 'Md':
                b = self.bmid
                v = s1[i-1] + v
                w = '-' + w
                i -= 1
        print max
        print v
        print w


class AffineGapPenalties:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.dataSet = "dataset_78_8.txt"
        #self.testSet = "lcs.txt"
        self.testSet = "affine_gap.txt"
        self.s1 = ''
        self.s2 = ''
     
        
    def read(self, f):
         
        s1 = f.readline().rstrip('\n')
        s2 = f.readline().rstrip('\n')
        
        self.s1 = s1
        self.s2 = s2
        
        #self.s1 = "PRTEINS"
        #self.s2 = "PRTWPSEIN"
        
        #self.s1 = "ADDFFFSWDFVDFSWDHF"
        #self.s2 = "DFFFSFVQIFQDFSHE"
            
        f.readline()
        
    def printVAR(self):
        s = ''
        s += "s1: " + self.s1 + "\n"
        s += "s2: " + self.s2 + "\n"
        
        return s

    def getFileName(self, test):
        if test:
            return self.testSet
        else:
            return self.dataSet

    def autoRun(self, f):
        self.read(f)
        print self.printVAR()
        
        from AffineGapPenalties import graph
        
        g = graph( len(self.s1), len(self.s2) )
        g.generateGraphs(self.s1, self.s2)
        g.computeScores()
        g.align()
        
def getFile(fileName):
    from os.path import expanduser
    home = expanduser("~")
    path = home + '//Downloads//' + fileName 
    #print path
    fileToOpen = open(path , 'r')
    return fileToOpen
       
if __name__ == '__main__':
    agp = AffineGapPenalties()
    test = True
    test = False
    f = getFile(agp.getFileName(test))    
    if test:
        f.readline()
    
    agp.autoRun(f)    