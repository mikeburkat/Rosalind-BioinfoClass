'''
Created on Oct 5, 2013

@author: Mike
'''
def getFile():
    from os.path import expanduser
    home = expanduser("~")
        
    fileName = raw_input("File name: ")
    path = home + '//Desktop//Rosalind//' + fileName 
    #print path
    fileToOpen = open(path , 'r')
    return fileToOpen


def findMotif(seq, mot):
    j = 0
    k = len(mot) - 1
    mot = mot[j:k]
    #print k
    locations = ''
    while k < len(seq):
        sbs = seq[j:k]
        #print sbs
        #print mot
        #print ''
        if (sbs == mot):
            locations = locations + str(j + 1) + ' ' 
            print locations
        j += 1
        k += 1
        
    return locations




if __name__ == '__main__':
    f = getFile()
    sequence = f.readline()
    motif = f.readline()
    f.close()
    
    print sequence
    print motif
    foundAt = findMotif(sequence, motif)
    print foundAt