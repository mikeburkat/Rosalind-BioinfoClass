'''
Created on Nov 19, 2013

@author: mike
'''

def RNAtoPROT(s):
    prot = ''
    j = 0
    k = 3
    
    
    codon = {'UUU' : 'F'   ,   'CUU' : 'L'  ,    'AUU' : 'I'   ,   'GUU' : 'V', 
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
    while k <= len(s):
        sbs = s[j:k]
        prot += codon[sbs]
        j += 3
        k += 3
        
    
    prot = prot.replace('*', '')
    return prot


def getFile():
    from os.path import expanduser
    home = expanduser("~")
    #fileName = raw_input("File name: ")
    #fileName = "protein_translate_data.txt"
    fileName = "dataset_18_3.txt"
    #fileName = ""
    path = home + '/Downloads/' + fileName 
    # print path
    fileToOpen = open(path , 'r')
    return fileToOpen

if __name__ == '__main__':
    f = getFile()
    #f.readline()
    seq = str(f.readline())
    #f.readline()
    #print f.readline()
    proteinSeq = RNAtoPROT(seq)
    
    print proteinSeq