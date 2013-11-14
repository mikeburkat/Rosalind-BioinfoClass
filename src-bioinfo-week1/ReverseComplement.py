'''
Created on Nov 12, 2013

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
    f = getFile()
    line = f.readline()
    revCompSeq = revComp(line)
    print revCompSeq