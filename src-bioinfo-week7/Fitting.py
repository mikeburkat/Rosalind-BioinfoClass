'''
Created on Dec 16, 2013

@author: Mike
'''



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
    #from GlobalAlignment import node
    
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.nodes = [[None for _ in range( m + 1 ) ] for _ in range( n + 1 )]
        self.backtrack = [[None for _ in range( m + 1 ) ] for _ in range( n + 1 )]
        #print len(self.nodes), len(self.nodes[0])
        
        
    def addNode(self, i, j, left, down):
        self.nodes[i][j] = node(left, down, 0)
        
        
    def printGraph(self):
        
        i = 0
        while i < len(self.nodes):
            j = 0
            
            header = '\t'
            row = '\t'
            while j < len(self.nodes[0]):
                if i == 0:
                    header += '  ' + self.nodes[i][j].down + '\t'
                    
                row += str(self.nodes[i][j].weight) + '\t'
                j += 1
            if i == 0:
                print header
            print row
            print self.nodes[i][j-1].left
            i += 1


    def generateGraph(self, s1, s2):
        i = 0
        while i < len(s1) + 1:
            j = 0
            while j < len(s2) + 1:
                
                if i == len(s1) and j == len(s2):
                    self.addNode(i, j, '', '')
                elif i == len(s1):
                    self.addNode(i, j, '', s2[j])
                elif j == len(s2):
                    self.addNode(i,j, s1[i], '')
                else:
                    self.addNode(i, j, s1[i], s2[j])
                
                j += 1
            i += 1
    
    def computeScores(self):
        nodes = self.nodes
        
        i = 1
        while i < self.n + 1:
            nodes[i][0].weight = nodes[i-1][0].weight 
            #nodes[i][0].backtrack = 'U'
            self.backtrack[i][0] = 'U' 
            i += 1
            
        #self.printGraph()
        
        j = 1
        while j < self.m + 1:
            nodes[0][j].weight = nodes[0][j-1].weight - 1
            #nodes[0][j].backtrack = 'L'
            self.backtrack[0][j] = 'L' 
            j += 1
            
        
        #self.printGraph()
        
        i = 1
        while i < self.n + 1:
            j = 1
            while j < self.m + 1:
                
                diag = nodes[i-1][j-1].weight + 1
                if nodes[i-1][j].left != nodes[i][j-1].down: 
                    diag = nodes[i-1][j-1].weight - 1
                    
                up = nodes[i-1][j].weight - 1
                left = nodes[i][j-1].weight - 1
                nodes[i][j].weight = max(up, left, diag)
                #print pam.getScore(nodes[i-1][j-1].left, nodes[i-1][j-1].down), diag
                #self.printGraph()
                
                if nodes[i][j].weight == up:
                    #nodes[i][j].backtrack == 'U'
                    self.backtrack[i][j] = 'U'
                elif nodes[i][j].weight == left:
                    #nodes[i][j].backtrack == 'L'
                    self.backtrack[i][j] = 'L'
                elif nodes[i][j].weight == diag:
                    #nodes[i][j].backtrack == 'D'
                    self.backtrack[i][j] = 'D' 
                #if nodes[i][j].weight == 0:
                #    self.backtrack[i][j] = 'O'
        
                j += 1
            i += 1
        
        #self.printGraph()
        
        
    def align(self, s1, s2):
        i = self.n
        j = self.m 
        backtrack = self.backtrack
        
        a = ''
        b = ''
        
        max = 0
        maxP = [0, 0]
        i = 0
        while i < self.n + 1:
            j = 0
            while j < self.m + 1:
                if max < self.nodes[i][j].weight:
                    max = self.nodes[i][j].weight
                    maxP = [i, j]
                j += 1
            i += 1
            
            
            
            
            
            
            
        sinksP = []
        sinkMax = 0
        
        i = maxP[0]
        j = self.m
        while i < self.n:
            #print i, j, self.nodes[i][j].weight
            if sinkMax < self.nodes[i][j].weight:
                sinkP = [i, j]
                sinkMax = self.nodes[i][j].weight
            i += 1
                
        i = sinkP[0]
        j = sinkP[1]
        
        while i != -1 and j != -1 and backtrack[i][j] != None and self.nodes[i][j].weight != 0:
            #print i, j
            #print backtrack[i][j]
            
            if backtrack[i][j] == 'U':
                i -= 1
                a = s1[i] + a
                b = '-' + b
                
            elif backtrack[i][j] == 'L':
                j -= 1
                a = '-' + a
                b = s2[j] + b
            elif backtrack[i][j] == 'O':
                i = 0
                j = 0
                
            else:
                i -= 1
                j -= 1
                a = s1[i] + a
                b = s2[j] + b
            
            
        #print i, j
            
            
            
            
            
            
        '''
        print max
        #print maxP
        i = maxP[0]
        j = maxP[1]
        
        for x in backtrack:
            print x
        
        
        while i != -1 and j != -1 and backtrack[i][j] != None and self.nodes[i][j].weight != 0:
            #print i, j
            #print backtrack[i][j]
            
            if backtrack[i][j] == 'U':
                i -= 1
                a = s1[i] + a
                b = '-' + b
                
            elif backtrack[i][j] == 'L':
                j -= 1
                a = '-' + a
                b = s2[j] + b
            elif backtrack[i][j] == 'O':
                i = 0
                j = 0
                
            else:
                i -= 1
                j -= 1
                a = s1[i] + a
                b = s2[j] + b
        '''
                
                
        
                
                
        print sinkMax
        print a
        print b
        





class Fitting:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.dataSet = "dataset_77_5.txt"
        #self.testSet = "lcs.txt"
        self.testSet = "fitting_alignment.txt"
     
        
    def read(self, f):
         
        s1 = f.readline().rstrip('\n')
        s2 = f.readline().rstrip('\n')
        
        self.s1 = s1
        self.s2 = s2
        
        #self.s1 = "GTAGGCTTAAGGTTA"
        #self.s2 = "TAGATA"
        
            
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
        
        from Fitting import graph
        
        g = graph( len(self.s1), len(self.s2) )
        
        g.generateGraph(self.s1, self.s2)
        #g.printGraph()
        g.computeScores()
        g.align(self.s1, self.s2)
        
        
        
        
def getFile(fileName):
    from os.path import expanduser
    home = expanduser("~")
    path = home + '//Downloads//' + fileName 
    #print path
    fileToOpen = open(path , 'r')
    return fileToOpen
       
if __name__ == '__main__':
    fa = Fitting()
    test = True
    test = False
    f = getFile(fa.getFileName(test))    
    if test:
        f.readline()
    
    fa.autoRun(f)    