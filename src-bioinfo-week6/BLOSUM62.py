'''
Created on Jan 13, 2014

@author: Mike
'''

class BLOSUM62:
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.order = []
        self.scores = []
        
        f = self.openFile()
        self.readFile(f)
        
        
    def openFile(self):
        from os.path import expanduser
        home = expanduser("~")
        fileName = "BLOSUM62.txt"
        path = home + '//Downloads//' + fileName 
        #print path
        f = open(path , 'r')
        return f
  
    def readFile(self, f):
        
        one = f.readline()
        all = f.readlines()
        
        order = one.rstrip().split(" ")
        order = filter(None, order)
        self.order = list( order )
        
        scores = []
        for l in all:
            matrix = l.rstrip().split(' ')
            matrix = filter(None, matrix)
            matrix = [x for x in matrix  if (x.isdigit() or x[0] == '-' and x[1:].isdigit())]
            scores.append( [int(i) for i in matrix] )
            
        self.scores = list( scores )
        
    def getPosition(self, x):
        i = 0
        while i < len(self.order):
            #print x, self.order[i], x == self.order[i]
            if x == self.order[i]:
                return i
            i += 1
        return None
        

    def getScore(self, a, b):
        i = self.getPosition(a)
        j = self.getPosition(b)
        
        if i == None or j == None:
            print a, b
        
        return self.scores[i][j]
            
            