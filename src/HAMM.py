'''
Created on Oct 5, 2013

@author: Mike
'''
def getFile():
    from os.path import expanduser
    home = expanduser("~")
        
    fileName = raw_input("File name: ")
    path = home + '//Desktop//Rosalind//' + fileName 
    print path
    fileToOpen = open(path , 'r')
    return fileToOpen


def pointMutations(sequence1, sequence2):
    count = 0
    index = 0
    while index < len(sequence1) and index < len(sequence2):
        if (sequence1[index] != sequence2[index]):
            count += 1
            
        index += 1
    return count
    
    



if __name__ == '__main__':
    
    f = getFile()
    seq1 = f.readline()
    seq2 = f.readline()
    f.close()
    
    print seq1, seq2
    dH = pointMutations(seq1, seq2)
    print dH
    