'''
Created on Oct 7, 2013

@author: Mike
'''

import sys

def getFile():
    from os.path import expanduser
    home = expanduser("~")
        
    fileName = raw_input("File name: ")
    path = home + '//Desktop//Rosalind//' + fileName 
    
    fileToOpen = open(path , 'r')
    return fileToOpen

def seperateFASTA(multiLines):
    sequences_FASTA = {}
    for line in multiLines:
        if line.startswith('>'):
            name = line[1:].rstrip('\n')
            sequences_FASTA[name] = ''
        else :
            sequences_FASTA[name] += line.rstrip('\n').rstrip('*')

    return sequences_FASTA

def findShortest(seqs):
    
    keyShrt = seqs.keys()[0]
    
    for key in seqs:
        if (len(seqs[key]) < len(seqs[keyShrt])):
            keyShrt = key
    return keyShrt



def fLS(sbs, seq):
    
    j = 0
    k = len(sbs) - 1
    s = sbs
    y = k
    count = 0

    while (len(s) > 0):
        y = k
        while y < len(sbs):
            s = sbs[j:y]
            #print s
            for x in seq:
                if (s in seq[x]):
                    count += 1
                    #print count
                    #print x
                    #print s
                    if (count == len(seq)):
                        return s
                
                
            count = 0    
            y += 1
            j += 1    
            
        j = 0
        k -= 1
    
    
    
    


''' 
    while len(s) > 0:
        while k < len(s):
            k = y
            for x in seq:
                sbs = s[j:k]
                print sbs
                if (sbs in seq[x]):
                    count += 1
                    print count
                    if (count == len(seq)):
                        return sbs
                j += 1
                k += 1
            j = 0    
            
            count = 0
        y -= 1
'''




if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    f = getFile()
    allLines = f.readlines()
    f.close()
    sequences = seperateFASTA(allLines)
    #for key in sequences:
    #    print key
    #    print sequences[key]
    shortest = findShortest(sequences)
    motif = fLS(sequences[shortest], sequences)
    print 'done'
    print len(motif), motif
    #                        rosalind_lcsm.txt
    
    #
    
    
    