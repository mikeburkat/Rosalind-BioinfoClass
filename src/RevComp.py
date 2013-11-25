'''
Created on Sep 28, 2013

@author: Mike
'''

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
        


if __name__ == '__main__':
    DNA = raw_input("Enter DNA sequence: ")
    #DNA = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
    revCompSeq = revComp(DNA)
    print revCompSeq