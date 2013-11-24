'''
Created on Nov 19, 2013

@author: mike
'''
import re


def DNAtoPROT(s, offset):
    prot = ''
    j = 0 + offset
    k = 3 + offset
    
    codon = {'TTT' : 'F'   ,   'CTT' : 'L'  ,    'ATT' : 'I'   ,   'GTT' : 'V', 
             'TTC' : 'F'   ,   'CTC' : 'L'  ,    'ATC' : 'I'   ,   'GTC' : 'V',
             'TTA' : 'L'   ,   'CTA' : 'L'  ,    'ATA' : 'I'   ,   'GTA' : 'V',
             'TTG' : 'L'   ,   'CTG' : 'L'  ,    'ATG' : 'M'   ,   'GTG' : 'V',
             'TCT' : 'S'   ,   'CCT' : 'P'  ,    'ACT' : 'T'   ,   'GCT' : 'A',
             'TCC' : 'S'   ,   'CCC' : 'P'  ,    'ACC' : 'T'   ,   'GCC' : 'A',
             'TCA' : 'S'   ,   'CCA' : 'P'  ,    'ACA' : 'T'   ,   'GCA' : 'A',
             'TCG' : 'S'   ,   'CCG' : 'P'  ,    'ACG' : 'T'   ,   'GCG' : 'A',
             'TAT' : 'Y'   ,   'CAT' : 'H'  ,    'AAT' : 'N'   ,   'GAT' : 'D',
             'TAC' : 'Y'   ,   'CAC' : 'H'  ,    'AAC' : 'N'   ,   'GAC' : 'D',
             'TAA' : '*'   ,   'CAA' : 'Q'  ,    'AAA' : 'K'   ,   'GAA' : 'E',
             'TAG' : '*'   ,   'CAG' : 'Q'  ,    'AAG' : 'K'   ,   'GAG' : 'E',
             'TGT' : 'C'   ,   'CGT' : 'R'  ,    'AGT' : 'S'   ,   'GGT' : 'G',
             'TGC' : 'C'   ,   'CGC' : 'R'  ,    'AGC' : 'S'   ,   'GGC' : 'G',
             'TGA' : '*'   ,   'CGA' : 'R'  ,    'AGA' : 'R'   ,   'GGA' : 'G',
             'TGG' : 'W'   ,   'CGG' : 'R'  ,    'AGG' : 'R'   ,   'GGG' : 'G',}

    codonRNA = {'UUU' : 'F'   ,   'CUU' : 'L'  ,    'AUU' : 'I'   ,   'GUU' : 'V', 
                'UUC' : 'F'   ,   'CUC' : 'L'  ,    'AUC' : 'I'   ,   'GUC' : 'V',
                'UUA' : 'L'   ,   'CUA' : 'L'  ,    'AUA' : 'I'   ,   'GUA' : 'V',
                'UUG' : 'L'   ,   'CUG' : 'L'  ,    'AUG' : 'M'   ,   'GUG' : 'V',
                'UCU' : 'S'   ,   'CCU' : 'P'  ,    'ACU' : 'T'   ,   'GCU' : 'A',
                'UCC' : 'S'   ,   'CCC' : 'P'  ,    'ACC' : 'T'   ,   'GCC' : 'A',
                'UCA' : 'S'   ,   'CCA' : 'P'  ,    'ACA' : 'T'   ,   'GCA' : 'A',
                'UCG' : 'S'   ,   'CCG' : 'P'  ,    'ACG' : 'T'   ,   'GCG' : 'A',
                'UAU' : 'Y'   ,   'CAU' : 'H'  ,    'AAU' : 'N'   ,   'GAU' : 'D',
                'UAC' : 'Y'   ,   'CAC' : 'H'  ,    'AAC' : 'N'   ,   'GAC' : 'D',
                'UAA' : '*'   ,   'CAA' : 'Q'  ,    'AAA' : 'K'   ,   'GAA' : 'E',
                'UAG' : '*'   ,   'CAG' : 'Q'  ,    'AAG' : 'K'   ,   'GAG' : 'E',
                'UGU' : 'C'   ,   'CGU' : 'R'  ,    'AGU' : 'S'   ,   'GGU' : 'G',
                'UGC' : 'C'   ,   'CGC' : 'R'  ,    'AGC' : 'S'   ,   'GGC' : 'G',
                'UGA' : '*'   ,   'CGA' : 'R'  ,    'AGA' : 'R'   ,   'GGA' : 'G',
                'UGG' : 'W'   ,   'CGG' : 'R'  ,    'AGG' : 'R'   ,   'GGG' : 'G',}
    
    while k < len(s):
        sbs = s[j:k]
        prot += codon[sbs]
        j += 3
        k += 3
    
    #prot = prot.replace('*', '')
    return prot



def findAllPatterns(s, pat, ori):
    al = []
    print ori
    for m in re.finditer( pat, s ):
        i = m.start()
        j = m.end()
        #print 'found at: ', i, j
        #print ori[i*3:j*3]
        al.append(ori[i*3:j*3])
    return al

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


def getFile():
    from os.path import expanduser
    home = expanduser("~")
    #fileName = raw_input("File name: ")
    #fileName = "peptide_encoding_data.txt"
    fileName = "dataset_18_6.txt"
    #fileName = ""
    path = home + '/Downloads/' + fileName 
    # print path
    fileToOpen = open(path , 'r')
    return fileToOpen

if __name__ == '__main__':
    f = getFile()
    #f.readline()
    seq = f.readline()
    seq = seq.rstrip()
    #f.readline()
    pattern = f.readline()
    
    #print f.readline()
    allReadingFrames = []
    protein1 = DNAtoPROT(seq, 0)
    protein2 = DNAtoPROT(seq, 1)
    protein3 = DNAtoPROT(seq, 2)
    rcSeq = revComp(seq)
    protein_1 = DNAtoPROT(rcSeq, 0)
    protein_2 = DNAtoPROT(rcSeq, 1)
    protein_3 = DNAtoPROT(rcSeq, 2)
    
    allReadingFrames.append(protein1)
    allReadingFrames.append(protein2)
    allReadingFrames.append(protein3)
    allReadingFrames.append(protein_1)
    allReadingFrames.append(protein_2)
    allReadingFrames.append(protein_3)
    
    pattern = pattern.rstrip()
    
    found = []
    rcfound = []
    found.append(findAllPatterns(protein1, pattern, seq))
    found.append(findAllPatterns(protein2, pattern, seq[1:]))
    found.append(findAllPatterns(protein3, pattern, seq[2:]))
    rcfound.append(findAllPatterns(protein_1, pattern, rcSeq))
    rcfound.append(findAllPatterns(protein_2, pattern, rcSeq[1:]))
    rcfound.append(findAllPatterns(protein_3, pattern, rcSeq[2:]))
    
    for a in found:
        for x in a:
            print x
            
    for a in rcfound:
        for x in a:
            print revComp(x)
    
    
    #for p in allReadingFrames:
        #print p
        #findAllPatterns(p, pattern, seq)
        
    
    
    