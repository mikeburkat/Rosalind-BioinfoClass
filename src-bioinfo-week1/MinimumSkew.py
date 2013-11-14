'''
Created on Nov 13, 2013

@author: Mike
'''

def computeSkew(sequence):
    sqews = []
    sq = 0
    for c in sequence:
        if ( c == 'C'):
            sq -= 1
        elif ( c == 'G'):
            sq += 1
        sqews.append(sq)
    return sqews



def findMaxSkew(s):
    i = 0
    minim = 0
    while (i < len(skew)):
        if ( skew[i] <= minim):
            minim = skew[i]
        i += 1
    
    mins = []
    i = 0
    while (i < len(skew)):
        if ( skew[i] == minim):
            mins.append(i+1)
        i += 1
    return mins


def getFile():
    from os.path import expanduser
    home = expanduser("~")
        
    fileName = raw_input("File name: ")
    path = home + '//Downloads//' + fileName 
    # print path
    fileToOpen = open(path , 'r')
    return fileToOpen

if __name__ == '__main__':
    f = getFile()
    #f.readline()
    seq = str(f.readline())
    f.close()
    
    skew = computeSkew(seq)
    #skew = computeSkew("TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT")
    #print len(seq)
    #print len(skew)
    
    data = findMaxSkew(skew)
    print data
    
    ans = ""
    for i in data:
        ans += str(i) + " "
    print ans
    
    i = 0
    while (i < len(skew)):
        print str(i + 1) +" "+ seq[i] + " " + str(skew[i])
        i += 1
    
    #   minimum_skew_data.txt