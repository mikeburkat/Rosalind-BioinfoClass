'''
Created on Nov 19, 2013

@author: mike
'''

pepList = ['']
weightList = []
rec = 6

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

def removeInconsistants(l):
    popList = []
    foundList = []
    for p in l:
        #print p, str(AAtoWeight(p))
        if not str(AAtoWeight(p)) in weightList:
            popList.append(p)
        elif str(AAtoWeight(p)) in weightList:
            if not str(AAtoWeight(p)) in foundList:
                foundList.append(str(AAtoWeight(p)))
            
    #print popList
    #print foundList
    
    
    for x in popList:
        l.remove( x )  
    
    for r in foundList:
        while r in weightList:
            weightList.remove( r )      
    
    return l
   
def removeCyclics(peps):
    unique = []
    for p in peps:
        cyclicIn = False
        x = len(p)
        #print p
        for i in range(len(p)):
            cyTest = p[i:] + p[:i]
            if cyTest in unique:
                cyclicIn = True
        
        if not cyclicIn:
            unique.append(p)
    return unique
    
    
def removeCyclics2(peps):
    noCyclics = list(peps)
    
    for p in peps:
        x = 0
        y = len(p)
        
        
        x += 1
        y += (y + 1) % (len(p))
        
        while x != 0:
            if x < y:
                print p[x:y]
                if p[x:y] in pepList:
                    print "in"
            elif x > y:
                print p[:y] + p[x:]
                if p[:y] + p[x:] in pepList:
                    print "in"
        
            x = (x + 1) % (len(p))
            y = (y + 1) % (len(p))
        
        
    return noCyclics
    
    

    
    
def expandList():
    global pepList
    
    #if rec == count:
    #    return
    
    allAA = ['G','S', 'A', 'P', 'V', 'T', 'C', 'I', 'N', 'D', 'K', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']
    
    sizeListforRemoval = []
    newPepList = []
    
    for a in allAA:
        for p in pepList:
            newPepList.append('' + p + a)
            
    #print newPepList
    noCyclics = removeCyclics(newPepList)
    #print noCyclics
    
    #print newPepList
    matchedPepList = removeInconsistants(noCyclics)
    #print matchedPepList
    if not len(matchedPepList) == 0:
        pepList = matchedPepList
    
    
def splitSeqtoInt(seq):
    for i in seq.split():
        weightList.append(int(i))
        
        
def convertToWeight(peps):
    l = []
    AAweight = { 'G' : 57, 'A' : 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C':103,'I' :113,
                'N' :114, 'D' :115,'K' :128,'E' :129, 'M' :131,'H' :137,
                'F' :147,'R' :156,'Y' :163,'W' :186 , '' : 0}
    
    for p in peps:
        j = 0
        s = ""
        while j < len(p):
            AA = p[j]
            s += str(AAweight[AA])+"-"
            j += 1
        if not s in l:
            l.append(s) 
    
    return l
        

    

def getFile():
    from os.path import expanduser
    home = expanduser("~")
    #fileName = raw_input("File name: ")
    fileName = "cycloseq_data.txt"
    #fileName = "dataset_20_3.txt"
    #fileName = ""
    path = home + '/Downloads/' + fileName 
    # print path
    fileToOpen = open(path , 'r')
    return fileToOpen

if __name__ == '__main__':
    f = getFile()
    f.readline()
    seq = f.readline()
    weightList = seq.split()
    
    #splitSeqtoInt(seq)
    weightList.remove('0')
    print weightList
    while not len(weightList) == 0:
        #print weightList
        expandList()
    
    print pepList
    print len(pepList)
    
    pepWeights = convertToWeight(pepList)
    
    print pepWeights
    print len(pepWeights)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    