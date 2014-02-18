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
        self.bmid = [[None for _ in range( m + 1 ) ] for _ in range( n + 1 )]
        
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
        self.generateGraph(self.middle, s1, s2, 'M')
        
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
        m = self.middle
        
        i = 0
        j = 0
        while i < self.n + 1:
            if i == 0:
                m[i][j].weight = 0
            elif i == 1:
                m[i][j].weight = - 5
            else:
                m[i][j].weight = m[i-1][j].weight - 5
            i += 1
        
        
        i = 0
        j = 0
        while j < self.m + 1:
            if j == 0:
                m[i][j].weight = 0
            elif j == 1:
                m[i][j].weight = - 5
            else:
                m[i][j].weight = m[i][j-1].weight - 5
            j += 1
        
        #self.printGraph(m, 'M')
        
        i = 0
        while i < self.n + 1:
            j = 0
            while j < self.m + 1:
                if i == 0 and j == 0:
                    self.bmid[i][j] = 'E'
                elif j == 0:
                    self.bmid[i][j] = 'd'
                    
                elif i == 0:
                    self.bmid[i][j] = 'r'
                    
                else:
                    diag = m[i-1][j-1].weight + self.bl.getScore(m[i][j].down, m[i][j].left)
                    up = m[i-1][j].weight - 5
                    left = m[i][j-1].weight - 5
                    m[i][j].weight = max(diag, up, left)
                    if m[i][j].weight == left:
                        self.bmid[i][j] = 'r'
                    elif m[i][j].weight == up:
                        self.bmid[i][j] = 'd'
                    else: 
                        self.bmid[i][j] = 'D'  
                    
                    
                j += 1
            i += 1
            
        #self.printGraph(m, 'M')
        
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
            elif b[i][j] == 'd':
                v = s1[i-1] + v
                w = '-' + w
                i -= 1
            elif b[i][j] == 'r':
                v = '-' + v
                w = s2[j-1] + w
                j -= 1
        print max
        print v
        print w
        
    def getMax(self):
        i = self.n
        j = self.m
        maxP = (i, j)
        max = self.middle[i][j].weight
        
        while i >= 0:
            if max < self.middle[i][j].weight:
                max = self.middle[i][j].weight
                maxP = (i, j)
                #print max , maxP
            i -= 1
        #print max , maxP
        return maxP
    
    def getMaxR(self, fi, s1 , s2):
        i = self.n - fi
        j = self.m
        maxP = (i, j)
        max = self.middle[i][j].weight
        
        #print max , maxP
        #print fi, j, s1[fi], s2[-j]
        
        diag = self.bl.getScore( s1[fi], s2[-j] )
        i -= 1
        #print self.middle[i][j].weight + diag, (i-1, j)
        
        if max < self.middle[i][j].weight:
            max = self.middle[i][j].weight
            maxP = (i, j)
            print max , maxP
        return maxP
    def getLastColumn(self):
        l = []
        i = 0
        j = self.m
        while i < self.n + 1:
            l.append(self.middle[i][j].weight)
            i += 1 
        
        return l
        

class MiddleEdge:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.dataSet = "dataset_79_12 (3).txt"
        #self.testSet = "lcs.txt"
        self.testSet = "linear_space.txt"
        self.s1 = ''
        self.s2 = ''
     
        
    def read(self, f):
         
        s1 = f.readline().rstrip('\n')
        s2 = f.readline().rstrip('\n')
        
        self.s1 = s1
        self.s2 = s2
        
        #self.s1 = "PLEASANTLY"
        #self.s2 = "MEASNLY"
        #self.s2 = "MEANLY"
        
        #self.s1 = "ADDFFFSWDFVDFSWDHF"
        #self.s2 = "DFFFSFVQIFQDFSHE"
            
        f.readline()
        
    def set(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
        
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

    def autoRun(self):
        #self.read(f)
        print self.printVAR()
        
        from MiddleEdge import graph
        
        
        fl = len(self.s2) / 2
        fs2 = self.s2[:fl]
        
        g = graph( len(self.s1), len(fs2) )
        g.generateGraphs(self.s1, fs2)
        g.computeScores()
        #g.align()
        fwdNode = g.getMax()
        fwdLast = g.getLastColumn()
        
        
        rs2 = self.s2[:fl-1:-1]
        #print rs2
        rs1 = self.s1[::-1]
        
        g = graph( len(rs1), len(rs2) )
        g.generateGraphs(rs1, rs2)
        g.computeScores()
        #g.align()
        revLast = g.getLastColumn()
        #print fwdLast
        
        revLast = revLast[::-1]
        #print revLast
        D = []
        H = []
        i = 0
        while i < len(fwdLast):
            D.append(fwdLast[i] + revLast[i])
            if i == 0: 
                H.append(0)
            else:
                H.append(fwdLast[i] + revLast[i-1])
            i += 1
        #print D
        #print H
        maxD = D[0]
        maxiD = 0
        maxiH = 0
        i = 0
        maxH = H[0]
        while i < len(D):
            if maxD < D[i]:
                maxD = D[i]
                maxiD = i
            elif maxH < H[i]:
                maxH = H[i]
                maxiH = i
            
            i += 1
        #print maxD, maxH, maxi
        
        if maxD < maxH:
            fwdNode = (maxiH, len(self.s2)/2)
            revNode = (maxiH, (len(self.s2)/2)+1)
        elif maxD >= maxH:
            fwdNode = (maxiD, len(self.s2)/2)
            revNode = (maxiD+1, (len(self.s2)/2)+1)
            
        #revNode = g.getMaxR( fwdNode[0], self.s1, self.s2 )
        #revNode = (len(self.s1) - revNode[0], fwdNode[1] + 1)
        #print fwdNode, revNode
        return ( fwdNode, revNode )
        
def getFile(fileName):
    from os.path import expanduser
    home = expanduser("~")
    path = home + '//Downloads//' + fileName 
    #print path
    fileToOpen = open(path , 'r')
    return fileToOpen
       
if __name__ == '__main__':
    me = MiddleEdge()
    test = True
    test = False
    f = getFile(me.getFileName(test))    
    if test:
        f.readline()
    
    me.autoRun(f)    