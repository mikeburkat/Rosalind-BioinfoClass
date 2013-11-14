'''
Created on Nov 13, 2013

@author: Mike
'''

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



def findMatchingPositions(seq, pat, mis):
    i = 0
    j = len(pat) - 1
    positions = []
    mm = []
    while (j < len(seq)):
        if (testMisMatch(seq[i:j], pat, mis)):
            positions.append(i)
            mm.append(seq[i:j])
        i += 1
        j += 1
    print mm
    return positions



def getFile():
    from os.path import expanduser
    home = expanduser("~")
    #fileName = raw_input("File name: ")
    fileName = "dataset_8_3.txt"
    #fileName = ""
    path = home + '//Downloads//' + fileName 
    # print path
    fileToOpen = open(path , 'r')
    return fileToOpen



if __name__ == '__main__':
    f = getFile()
    #f.readline()
    pattern = str(f.readline())
    seq = str(f.readline())
    mis = int(f.readline())
    #pattern = "ATTCTGGA"
    #seq = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
    #mis = 3
    
    f.close()
    
    res = findMatchingPositions(seq, pattern, mis)
    ans = ""
    for i in res:
        ans += str(i) + " "
    print ans
    
    
    
    #skew = computeSkew("TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT")
    #print len(seq)
    #print len(skew)
    
    