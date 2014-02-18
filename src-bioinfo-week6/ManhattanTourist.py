'''
Created on Dec 16, 2013

@author: Mike
'''

class ManhattanTourist:
    '''
    classdocs
    
    Adapted to use the diagonal
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.dataSet = "dataset_72_9.txt"
        self.testSet = "man_tou.txt"
        #self.testSet = "longest_path_1.txt"
        self.n = 0
        self.m = 0
        self.down = []
        self.right = []
        self.diagonal = []
        
    def prMat(self, mat):
        
        for x in mat:
            print x
        print
    
    def manhattanTourist(self, n, m, down, right):
        matrix = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        i = 0
        j = 0
        
        for x in range(m):
            #print x
            matrix[0][x+1] = matrix[0][x] + int(right[0][x])
            #self.prMat(matrix)
            
        for y in range(n):
            #print y
            matrix[y+1][0] = matrix[y][0] + int(down[y][0])
            #self.prMat(matrix)
        
        i = 1
        j = 1
            
        while i in range(n+1):
            j = 1
            while j in range(m+1):
                #print i, j
                left = matrix[i][j-1] + int(right[i][j-1])
                up = matrix[i-1][j] + int(down[i-1][j])
                diag = matrix[i-1][j-1] + int(self.diagonal[i-1][j-1])
                #print left, matrix[i][j-1], int(right[i][j-1])
                #print up, matrix[i-1][j], int(down[i-1][j])
                matrix[i][j] = max(up, left, diag)
                self.prMat(matrix)
                
                j += 1
            i += 1
        
        self.prMat(matrix)
        
        return matrix
        
            
    def read(self, f):
         
        n = f.readline()
        m = f.readline()
        
        self.n = int(n)
        self.m = int(m)
        
        for x in range(self.n):
            temp = f.readline()
            self.down.append(temp.rstrip("\n").split(" "))
            
        f.readline()
        
        for x in range(self.n + 1):
            temp = f.readline()
            self.right.append(temp.rstrip("\n").split(" "))
        
        self.diagonal = [[5, 0, 2, 1], [8, 4, 3, 0], [10, 8, 9, 5], [5, 6, 4, 7]]
        
        
    def printVAR(self):
        s = ''
        s += "n: " + str(self.n) + "\n"
        s += "m: " + str(self.m) + "\n"
        
        print s
        
        for x in self.down:
            print x
        
        for x in self.right:
            print x
        
        return s

    def getFileName(self, test):
        if test:
            return self.testSet
        else:
            return self.dataSet

    def autoRun(self, f):
        self.read(f)
        self.printVAR()
        self.manhattanTourist(self.n, self.m, self.down, self.right)
        
        
def getFile(fileName):
    from os.path import expanduser
    home = expanduser("~")
    path = home + '//Downloads//' + fileName 
    #print path
    fileToOpen = open(path , 'r')
    return fileToOpen
       
if __name__ == '__main__':
    mt = ManhattanTourist()
    test = True
    #test = False
    f = getFile(mt.getFileName(test))    
    #if test:
        #f.readline()
    
    mt.autoRun(f)    