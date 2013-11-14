'''
Created on Nov 13, 2013

@author: Mike
'''

kMerArray = []
kMerDict = {}
per = []

            
def allKmers(k, set):
    if (k == 0):
        #kMerArray.append(kMer(set, 0))
        kMerDict[set] = 0
    else:
        allKmers(k-1, set + "A")
        allKmers(k-1, set + "T")
        allKmers(k-1, set + "C")
        allKmers(k-1, set + "G")
        
        
        
def revComp(sequence):
    revCompS = ''
    for c in sequence:
        if c == 'A':
            revCompS = 'T' + revCompS
        if c == 'T':
            revCompS = 'A' + revCompS
        if c == 'C':
            revCompS = 'G' + revCompS
        if c == 'G':
            revCompS = 'C' + revCompS
        if c == 'N':
            revCompS = c + revCompS
            
    return revCompS        
        
        
        
        


def permutations(s, i, m):
    if (m == 0):
        global per
        found = False
        for p in per:
            if (p == s):
                found = True
        if (not found ):
            per.append(s)
            
    else:
        x = i
        while (x + m < len(s) + 1):
            if (s[x]  == "A"):
                permutations(s[:x]+"T"+s[x+1:], x, m-1)
                permutations(s[:x]+"C"+s[x+1:], x, m-1)
                permutations(s[:x]+"G"+s[x+1:], x, m-1)
            elif (s[x] == "C"): 
                permutations(s[:x]+"A"+s[x+1:], x, m-1)
                permutations(s[:x]+"T"+s[x+1:], x, m-1)
                permutations(s[:x]+"G"+s[x+1:], x, m-1)
            elif (s[x] == "G"): 
                permutations(s[:x]+"T"+s[x+1:], x, m-1)
                permutations(s[:x]+"C"+s[x+1:], x, m-1)
                permutations(s[:x]+"A"+s[x+1:], x, m-1)
            elif (s[x] == "T"): 
                permutations(s[:x]+"C"+s[x+1:], x, m-1)
                permutations(s[:x]+"G"+s[x+1:], x, m-1)
                permutations(s[:x]+"A"+s[x+1:], x, m-1)
            
            x += 1
    

def findKmers(seq, k, mis):
    x = 0
    y = k
    while (y < len(seq)):
        global per
        per = []
        
        permutations(seq[x:y], 0, mis)
        #print per
        
        for p in per:
            if (kMerDict.has_key(p)):
                kMerDict[p] += 1
            else:
                kMerDict[p] = 1
        
        x += 1
        y += 1
    


def findMostFrequent():
    maxi = 0
    kmers = ""
    for x in kMerDict:
        revCount = 0
        if (kMerDict.has_key(revComp(x))):
            revCount = kMerDict[revComp(x)]
        if ( maxi < kMerDict[x] + revCount):
            maxi = kMerDict[x] + revCount
            kmers = x + " " + revComp(x)
    return kmers




def getFile():
    from os.path import expanduser
    home = expanduser("~")
    #fileName = raw_input("File name: ")
    #fileName = "frequent_words_mismatch_complement.txt"
    fileName = "dataset_8_51.txt"  #AAAACCCCCC ACACCCCAAA ACCCCCCGCA CCCTCGCATA 
    #fileName = ""
    path = home + '//Downloads//' + fileName 
    # print path
    fileToOpen = open(path , 'r')
    return fileToOpen

if __name__ == '__main__':
    f = getFile()
    #f.readline()
    seq = str(f.readline())
    k = int(f.readline())
    mis = int(f.readline())
    #pattern = "ATTCTGGA"
    #k = 4
    #seq = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    #mis = 1
    

    
    allKmers(k, "")
    #print len(kMerArray)
    print len(kMerDict)
    findKmers(seq, k, mis)
    #print kMerDict
    
    result = findMostFrequent()
    print result
    
    