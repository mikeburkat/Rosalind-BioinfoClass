'''
Created on Nov 13, 2013

@author: Mike
'''

kMerArray = []

class kMer:
    def __init__(self, sequence, frequency):
        self.sequence = sequence
        self.frequency = frequency
    def addOne(self):
        self.frequency += 1


class nucleoTree:
    def __init__(self, nucleotide, frequency):
        self.frequency = frequency
        self.nuclotide = nucleotide
        self.children = []
        
        def addChild(self, obj):
            self.children.append(obj)
            
        def addFound():
            self.frequency += 1
            
            
def allKmers(k, set):
    if (k == 0):
        kMerArray.append(kMer(set, 0))
    else:
        allKmers(k-1, set + "A")
        allKmers(k-1, set + "T")
        allKmers(k-1, set + "C")
        allKmers(k-1, set + "G")


def testMisMatch(seq, pat, mis):
    x = 0
    mismatch = 0
    #Sprint seq, pat
    for i in seq:
        if (not pat[x] == i ):
            #print pat[x], i
            mismatch += 1
            if ( mismatch > mis ):
                #print "False"
                return False
        x += 1
    return True



def findKmers(s, k, m):
    
    x = 0
    while ( x < len(kMerArray)):
        i = 0
        j = k
        #print kMerArray[x].sequence
        while (j < len(s)):
            #print kMerArray[x].sequence, s[i:j]
            if ( testMisMatch(kMerArray[x].sequence, s[i:j], m)):
                kMerArray[x].addOne()
            i += 1
            j += 1
        x += 1
    
    
def findMostFrequent(a):
    maxi = 0
    kmers = ""
    for x in a:
        if ( maxi < x.frequency):
            maxi = x.frequency
    for x in a:
        if (maxi == x.frequency):
            kmers = kmers + x.sequence + " "
    return kmers



def getFile():
    from os.path import expanduser
    home = expanduser("~")
    #fileName = raw_input("File name: ")
    #fileName = "frequent_words_mismatch_data.txt"
    fileName = "dataset_8_4.txt"  #AAAACCCCCC ACACCCCAAA ACCCCCCGCA CCCTCGCATA 
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
    #seq = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
    #mis = 3
    

    
    allKmers(k, "")
    #print len(kMerArray)
    findKmers(seq, k, mis)
    result = findMostFrequent(kMerArray)
    print result
    
    
    
    
    
    
    