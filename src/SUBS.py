'''
Created on Oct 5, 2013

@author: Mike
'''
def getFile():
    from os.path import expanduser
    home = expanduser("~")
        
    fileName = raw_input("File name: ")
    path = home + '//Downloads//' + fileName 
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
            locations = locations + str(j) + ' ' 
            #print locations
        j += 1
        k += 1
        
    return locations


    #dataset_3_51.txt

if __name__ == '__main__':
    f = getFile()
    motif = f.readline()
    sequence = f.readline()
    f.close()
    
    foundAt = findMotif(sequence, motif)
    print foundAt