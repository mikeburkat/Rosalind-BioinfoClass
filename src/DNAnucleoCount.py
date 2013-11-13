'''
Created on Sep 28, 2013

@author: Mike
'''

def countDNA(sequence):
    A = 0
    T = 0
    C = 0
    G = 0
    notBase = 0
    for c in sequence:
        if c == 'A':
            A = A + 1
        elif c == 'T':
            T = T + 1
        elif c == 'C':
            C = C + 1
        elif c == 'G':
            G = G + 1    
        else:
            notBase =+ 1
    #print 'A= ' , A
    #print 'T= ' , T
    #print 'C= ' , C
    #print 'G= ' , G
    #print 'Not bases= ' , notBase
    DNAcount = [A,T,C,G]
    return DNAcount
    
if __name__ == '__main__':
    DNA = raw_input("Enter DNA sequence: ")
    #DNA = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
    bases = countDNA(DNA)
    print '[A,T,C,G]', bases
    

