'''
Created on Oct 5, 2013

@author: Mike
'''

'''
class FASTA:
    def __init__(self, ID='<empty>', sequence='<empty>'):
        self.ID = ID
        self.sequence = sequence
    
    def set_ID(self, ID):
        self.ID = ID
    
    def get_ID(self): 
        return self.ID
    
    def set_seq(self, sequence):
        self.sequence = sequence
        
    def get_seq(self): 
        return self.sequence
    
    def __iter__(self):
        yield [ID, sequence]
'''



def getFile():
    from os.path import expanduser
    home = expanduser("~")
        
    fileName = raw_input("File name: ")
    path = home + '//Desktop//Rosalind//' + fileName 
    #print path
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

def computeGC(seq):
    A = 0
    T = 0
    C = 0
    G = 0
    length = 0
    notBase = 0
    for c in seq:
        if c == 'A':
            A += 1
            length += 1
        elif c == 'T':
            T += 1
            length += 1
        elif c == 'C':
            C += 1
            length += 1
        elif c == 'G':
            G += 1    
            length += 1
        else:
            notBase =+ 1
    #print A, T, C, G
    #print G+C
    #print length
    
    GC = ((C+0.0+G+0.0)*100) / (length+0.0)
    
    return GC


def percentGC(sF):
    allGC = {}
    #print sF
    for key in sF:
        allGC[key] = computeGC(sF[key])
    return allGC

    

def findHighestGC(toFind):
    highestName = ''
    highestValue = 0
    for index in toFind:
        if highestValue < toFind[index]:
            highestName = index
            highestValue = toFind[index]
    
    return [highestName, highestValue]



if __name__ == '__main__':
    f = getFile()
    allLines = f.readlines()
    f.close()
    sequences = seperateFASTA(allLines)
    contentGC = percentGC(sequences)
    highestGC = findHighestGC(contentGC)
    
    print highestGC[0]
    print highestGC[1]
    
    #print sequences
    #print contentGC
    
    