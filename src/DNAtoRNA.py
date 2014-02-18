'''
Created on Sep 28, 2013

@author: Mike
'''

def DNAtoRNA(DNA):
    #for c in sequence:
    RNA = DNA.replace('T', 'U')    
    
    return RNA


if __name__ == '__main__':
    DNA = raw_input("Enter DNA sequence: ")
    #DNA = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
    seqRNA = DNAtoRNA(DNA)
    print seqRNA
    