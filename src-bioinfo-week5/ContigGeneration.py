'''
Created on Dec 8, 2013

@author: Mike
'''

class ChangeProblem:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.dataSet = "dataset_59_5 (1).txt"
        self.testSet = "contig_generation_3.txt"
        self.change = 0
        self.coins = []
        
        
    
    
    def DPChange(self, money, coins):
        MinNumCoins = [float("inf")] * (money + 1)
        MinNumCoins[0] = 0
        #print len(MinNumCoins)
        m = 1
        while m < len(MinNumCoins):
            #print m
            #print MinNumCoins
            for c in coins:
                if m >= int(c):
                    if MinNumCoins[ m - int(c) ] + 1 < MinNumCoins[m]:
                        MinNumCoins[m] = MinNumCoins[ m - int(c) ] + 1
                    
            m += 1
        #print MinNumCoins
        #print MinNumCoins[money]
        return MinNumCoins[money]
            
    def read(self, f):
         
        l1 = f.readline()
        l2 = f.readline()
        
        l1 = '17868'
        l2 = '22,5,3,1'
        
        self.change = int(l1)
        self.coins = l2.split(",")
        
    def printVAR(self):
        s = ''
        s += "Change: " + str(self.change) + "\n"
        s += "Coins: " + str(self.coins) + "\n"
        return s

    def getFileName(self, test):
        if test:
            return self.testSet
        else:
            return self.dataSet

    def autoRun(self, f):
        self.read(f)
        #print self.printVAR()
        print self.DPChange(self.change, self.coins)
        
        
def getFile(fileName):
    from os.path import expanduser
    home = expanduser("~")
    path = home + '//Downloads//' + fileName 
    #print path
    fileToOpen = open(path , 'r')
    return fileToOpen
       
if __name__ == '__main__':
    cp = ChangeProblem()
    test = True
    #test = False
    f = getFile(cp.getFileName(test))    
    if test:
        f.readline()
    
    cp.autoRun(f)    
        