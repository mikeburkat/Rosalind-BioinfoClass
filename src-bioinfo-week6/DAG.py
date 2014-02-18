'''
Created on Dec 16, 2013

@author: Mike
'''

class DAG:
    '''
    classdocs
    '''
    
    class nodeDAG:
        def __init__(self, o, d, w):
            self.ori = o
            self.mid = []
            self.dst = d
            self.weight = w
            
        def __str__(self):
            s = str(self.ori) + '->' + str(self.dst) + ' : ' + str(self.weight) + ' '
            return s
        
        
        
        
    class graphDAG:
        def __init__(self):
            self.nodes = []
            self.queue = []
            self.paths = []
        
        def addNode(self, n):
            self.nodes.append(n)
            
        def addNodesToQueue(self, ori):
            for x in self.nodes:
                if ori == x.ori:
                    self.queue.append(x)
                    
        def printQueue(self):
            for x in self.queue:
                print x
            
        def addToPath(self, n):
            toADD = []
            
            
            for x in self.paths:
                #print x.dst, n.ori, x.dst == n.ori
                if x.dst == n.ori:
                    
                    temp = DAG.nodeDAG(x.ori, n.dst, x.weight + n.weight)
                    temp.mid = list(x.mid)
                    temp.mid.append(n.ori)
                    toADD.append(temp)
            
            self.paths.append(n)
            for x in toADD:
                self.paths.append(x)
                
        
        def printPaths(self):
            print "here"
            for x in self.paths:
                print x, x.mid
                
            
        
        def findLongestPath(self, ori, dst):
            self.addNodesToQueue(ori)
            #self.printQueue()
            while len(self.queue) > 0:
                temp = self.queue.pop(0)
                #print len(self.queue), temp
                
                self.addToPath(temp)
                self.addNodesToQueue(temp.dst)
                
            #self.printPaths()
            
            return self.paths
        
        
        
            

    def __init__(self):
        '''
        Constructor
        '''
        self.dataSet = "dataset_74_7.txt"
        #self.testSet = "lcs.txt"
        self.testSet = "longest_path_in_DAG.txt"
        self.dataNodes = []
        self.pathORI = 0
        self.pathDST = 0
        self.gDAG = self.graphDAG()
        
    def read(self, f):
        
        self.pathORI = int(f.readline())
        self.pathDST = int(f.readline())
        
        all = f.readlines()
        for x in all:
            if x == "\n":
                break
            temp = x.split('->')
            temp2 = temp[1].split(':')
            o = int(temp[0])
            d = int(temp2[0])
            w = int(temp2[1])
            self.gDAG.addNode( self.nodeDAG( o, d, w ) )
    
    def findLongest(self, allPaths, o, d):
        longest = DAG.nodeDAG(0, 0, 0)
        for x in allPaths:
            #print x.ori, o, x.ori == o, x.dst, d, x.dst == d
            if (x.ori == o and x.dst == d):
                #print 'contender', x, x.mid
                if x.weight > longest.weight:
                    
                    longest = x
                    #print 'new longest', longest, longest.mid
        return longest
    
    def printANS(self, ans):
        s = ''
        s += str(ans.weight) + "\n"
        s += str(ans.ori)
        for x in ans.mid:
            s += "->" + str(x)
        s += "->" + str(ans.dst)
        
        return s
        
    def printVAR(self):
        s = ''
        print "ori =", self.pathORI
        print "dst =", self.pathDST 
        for x in self.gDAG.nodes:
            print x.ori, "->", x.dst, ":", x.weight
        
        return s

    def getFileName(self, test):
        if test:
            return self.testSet
        else:
            return self.dataSet

    def autoRun(self, f):
        self.read(f)
        print self.printVAR()
        
        allPaths = self.gDAG.findLongestPath(self.pathORI, self.pathDST)
        
        ans = self.findLongest(allPaths, self.pathORI, self.pathDST)
        
        print self.printANS(ans)
        
        
        
def getFile(fileName):
    from os.path import expanduser
    home = expanduser("~")
    path = home + '//Downloads//' + fileName 
    #print path
    fileToOpen = open(path , 'r')
    return fileToOpen
       
if __name__ == '__main__':
    dag = DAG()
    test = True
    test = False
    f = getFile(dag.getFileName(test))    
    if test:
        f.readline()
    
    dag.autoRun(f)    