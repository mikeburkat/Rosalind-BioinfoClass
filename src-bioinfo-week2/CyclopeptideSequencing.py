'''
Created on Nov 19, 2013

@author: mike
'''

allFragments = []


def compareSpec(weights, testList):
    allIN = True
    
    for w in weights:
        if not w in testList:
            allIN = False
            break
        else:
            testList.remove(w)
    
    return allIN


def AAtoWeight(s):

    AAweight = { 'G' : 57, 'A' : 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C':103,'I' :113,
                'L' :113, 'N' :114, 'D' :115,'K' :128,'Q' :128,'E' :129, 'M' :131,'H' :137,
                'F' :147,'R' :156,'Y' :163,'W' :186 , '' : 0}
            
    j = 0
    weight = 0
    while j < len(s):
        AA = s[j]
        weight += AAweight[AA]
        j += 1
    
    return weight
    
    
def allPossibleLinearFragments(s):
    linFrag = []
    
    size = 1
    while size <= len(s):
        x = 0
        while x + size <= len(s):
            linFrag.append( s[x:x+size] )
            x += 1
        size += 1
    
    return linFrag
    


def removeInconsistent3(pep, wLst):
    global allFragments
    trimmed = []
    
    for p in pep:
        testList = list(wLst)
        allFragments = []
        allFragments = allPossibleLinearFragments(p)
        #print allFragments
        
        weights = []
        for w in allFragments:
            weights.append( AAtoWeight(w) )
        #print weight
        #print wLst
        oneFalse = True
        #print testList
        #print weights
        if compareSpec(weights, testList):
            #print p
            #print weights
            #print True
            trimmed.append(p)
        
        
    return trimmed


def expand(pep):
    allAA = ['G','S', 'A', 'P', 'V', 'T', 'C', 'I', 'N', 'D', 'K', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']
    newPepList = []
    
    for p in pepList:
        for a in allAA:
            newPepList.append('' + p + a)

    return newPepList




def printMyPepList(pep):
    s = ""
    for p in pep:
        x = 0
        
        while x < len(p):
            s += str ( AAtoWeight( p[x] ) )
            if x+1 != len(p):
                s += "-"
            
            
            x += 1
        s += " "
    return s
    


def splitSeqtoInt(seq):
    wIL = []
    for i in seq:
        #print i
        wIL.append(int(i))
    return wIL


def getFile():
    from os.path import expanduser
    home = expanduser("~")
    #fileName = raw_input("File name: ")
    fileName = "cycloseq_data.txt"
    #fileName = "dataset_22_4_1.txt"
    #fileName = ""
    path = home + '/Downloads/' + fileName 
    # print path
    fileToOpen = open(path , 'r')
    return fileToOpen

if __name__ == '__main__':
    weightList = []
    f = getFile()
    f.readline()
    seq = f.readline()
    weightList = seq.split()
    weightList = splitSeqtoInt(weightList)
    print weightList
    #weightList = [0, 113, 128, 186, 241, 299, 314, 427]
    #weightList = [0, 113, 114, 128, 129, 129, 227, 242, 242, 257, 258, 355, 356, 371, 371, 386, 484, 484, 485, 499, 500, 613]
    #weightList = [ 0, 97, 97, 99, 101, 103, 196, 198, 198, 200, 202, 295, 297, 299, 299, 301, 394, 396, 398, 400, 400, 497]
    pepList = ['']
    
    x = 0
    
    while x < 10 :
    
        pepList = expand(pepList)
        
        pepList = removeInconsistent3(pepList, weightList)
        
        print pepList
        print len(pepList)
        
        x += 1
        
      
    print printMyPepList(pepList)
    
    
    