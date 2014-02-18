'''
Created on Jan 15, 2014

@author: Mike
'''

class LinearSpaceAlignment:
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
        
        self.s1 = "PLEASANTLY"
        #self.s2 = "MEASNLY"
        self.s2 = "MEANLY"
        
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
        from MiddleEdge import MiddleEdge
        
        me = MiddleEdge()
        queue = []
        queue.append((self.s1, self.s2))
        backtrack = {}
        
        
        while len(backtrack) != len(self.s2):
            print len(backtrack)
            
            q = queue.pop(0)
            
            
            me.set(q[0], q[1])
            edge = me.autoRun()
            print edge
            
            backtrack[edge[0][1]] = edge
            
            f1 = q[0][:edge[0][1]]
            f2 = q[1][:edge[0][0]]
            queue.insert(0, (f1, f2))
            print f1, f2
            
            r1 = self.s1[edge[1][1]:]
            r2 = self.s2[edge[1][0]:]
            queue.insert(0, (f1, f2))
            print r1, r2
        
        
        
        
def getFile(fileName):
    from os.path import expanduser
    home = expanduser("~")
    path = home + '//Downloads//' + fileName 
    #print path
    fileToOpen = open(path , 'r')
    return fileToOpen
       
if __name__ == '__main__':
    lsa = LinearSpaceAlignment()
    test = True
    #test = False
    f = getFile(lsa.getFileName(test))    
    if test:
        f.readline()
    
    lsa.autoRun(f)    