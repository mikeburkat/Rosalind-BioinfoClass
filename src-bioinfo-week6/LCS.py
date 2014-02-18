'''
Created on Dec 16, 2013

@author: Mike
'''

class LongestCommonSubstring:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.dataSet = "dataset_74_5 (1).txt"
        #self.testSet = "lcs.txt"
        self.testSet = "longest_common_subsequence.txt"
        self.n = 0
        self.m = 0
        self.down = []
        self.right = []
        self.diagonal = []
        self.backtrack = []
        self.s1 = ''
        self.s2 = ''
        
    def prMat(self, mat):
        s1 = '   ['
        for x in self.s1:
            s1 += x + ', '
        
        print s1[:-2] + ']'
        
        
        for x, y in zip(mat, self.s2+' '):
            print y, x
        print
        
        
    def findDiagonalMatrix(self, s1, s2):
        matrix = [[0 for _ in range(len(s1))] for _ in range(len(s2))]
        #self.prMat(matrix)
        
        i = 0
        j = 0
        
        while i < len(s1):
            j = 0
            while j < len(s2):
                
                if s1[i] == s2[j]:
                    matrix[j][i] = 1
                    #self.prMat(matrix)
                
                j += 1
            i += 1
        #self.prMat(matrix)
        return matrix

        
        
    def LCS(self, s1, s2, diagonal):    
        matrix = [[0 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]
        self.backtrack = [[0 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]
        
        i = 1
        j = 1
            
        while i < len(s2)+1:
            j = 1
            while j < len(s1)+1:
                #print i, j
                left = matrix[i][j-1]
                up = matrix[i-1][j]
                diag = matrix[i-1][j-1] + diagonal[i-1][j-1]
                matrix[i][j] = max(up, left, diag)
                
                if (matrix[i][j] - 1 == matrix[i-1][j-1] and diagonal[i-1][j-1] == 1):
                    self.backtrack[i][j] = 'D'
                elif (max(up, left, diag) == up):
                    self.backtrack[i][j] = 'U'
                else:
                    self.backtrack[i][j] = 'L'
                
                
                
                #self.prMat(matrix)
                
                j += 1
            i += 1
        
        #self.prMat(matrix)
        #self.prMat(self.backtrack)
        
        return matrix
        
    def findLCS(self, backtrack, s1, i, j):
        
        s = ''
        
        while i != 0 and j != 0:
            print i, j
            print backtrack[i][j]
            
            if backtrack[i][j] == 'U':
                i -= 1
            elif backtrack[i][j] == 'L':
                j -= 1
            else:
                i -= 1
                j -= 1
                s = s1[j] + s
        print len(s), s
        
    def read(self, f):
         
        s1 = f.readline()
        s2 = f.readline()
        
        self.s1 = s1
        self.s2 = s2
        
        #self.s1 = "AACCTTGG"
        #self.s2 = "ACACTGTGA"
            
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
        self.diagonal = self.findDiagonalMatrix(self.s1, self.s2)
        map = self.LCS(self.s1, self.s2, self.diagonal)
        self.findLCS(self.backtrack, self.s1, len(self.s2), len(self.s1))
        
        
        
def getFile(fileName):
    from os.path import expanduser
    home = expanduser("~")
    path = home + '//Downloads//' + fileName 
    #print path
    fileToOpen = open(path , 'r')
    return fileToOpen
       
if __name__ == '__main__':
    lcs = LongestCommonSubstring()
    test = True
    test = False
    f = getFile(lcs.getFileName(test))    
    if test:
        f.readline()
    
    lcs.autoRun(f)    