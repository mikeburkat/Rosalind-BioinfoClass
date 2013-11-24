'''
Created on Nov 19, 2013

@author: mike
'''


weightList = []
weightIntList = []
allFragments = []

def splitSeqtoInt(seq):
    for i in seq.split():
        weightIntList.append(int(i))

def expand(pepList):
    #if rec == count:
    #    return
    
    allAA = ['G','S', 'A', 'P', 'V', 'T', 'C', 'I', 'N', 'D', 'K', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']
    
    newPepList = []
    
    for a in allAA:
        print a
        for p in pepList:
            print p
            newPepList.append('' + p + a)
    
    return newPepList


def allPossibleFragments(s, size):
    global allFragments
    if size == 0:
        allFragments.append(s)
        return
    
    x = 0
    y = len(s) - size
    allFragments.append(s[x:y])
    
    x += 1
    y += 1
    while x != 0:
        #print x, y
        if x < y:
            #print s[x:y]
            allFragments.append(s[x:y])
        elif x > y:
            #print s[:y] + s[x:]
            allFragments.append( (s[:y] + s[x:]) )
        
        x = (x + 1) % (len(s))
        y = (y + 1) % (len(s))
        allPossibleFragments(s, size - 1)
    return allFragments
                               
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

def compareSpec(spec):
    checkList = weightIntList
    for i in spec:
        if not i in checkList:
            return False
        elif i in checkList:
            checkList.remove(i)
    
    return True

def loop(pepList):
    global allFragments
    pepList = expand(pepList)
    print pepList
    toRemove = []
    toExpand = []
    for p in pepList:
            allFragments = []
            specTheoFragments = allPossibleFragments(p, len(p))
            spectrum = []
            for a in allFragments:
                spectrum.append( AAtoWeight(a) )
            spectrum.sort(cmp=None, key=None, reverse=False)
            spec = ''
            for sp in spectrum:
                spec += str(sp) + " "
            #print spec
            if compareSpec(spectrum):
                print p
                toExpand.append(p)
                print toExpand
            else:
                toRemove.append(p)
    print toExpand
    loop(pepList)
    

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
    global allFragments 
    f = getFile()
    f.readline()
    seq = f.readline()
    weightList = seq.split()
    splitSeqtoInt(seq)
    
    pepList = ['']
    
    
    loop(pepList)




    
    #CYCLOPEPTIDESEQUENCING(Spectrum)
    #    List <- {0-peptide}
    #    while List is nonempty
    #        List <- Expand(List)
    #        for each peptide Peptide in List
    #            if Cyclospectrum(Peptide) = Spectrum
    #                output Peptide
    #                remove Peptide from List
    #            else if Peptide is not consistent with Spectrum
    #                remove Peptide from List
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    