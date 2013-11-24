'''
Created on Nov 19, 2013

@author: mike
'''

allFragments = []
spectrum = []

def AAtoWeight(s):

    AAweight = { 'G' : 57, 'A' : 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C':103,'I' :113,
                'L' :113, 'N' :114, 'D' :115,'K' :128,'Q' :128,'E' :129, 'M' :131,'H' :137,
                'F' :147,'R' :156,'Y' :163,'W' :186 , '' : 0}
            
    j = 0
    weight = 0
    while j < len(s):
        AA = s[j]
        weight += AAweight[AA]
        j += 1
    
    return weight
    
    
    
def allPossibleFragments(s, size):
    if size == 0:
        allFragments.append(s)
        return
    
    x = 0
    y = len(s) - size
    allFragments.append(s[x:y])
    
    x += 1
    y += 1
    while x != 0:
        #print x, y
        if x < y:
            #print s[x:y]
            allFragments.append(s[x:y])
        elif x > y:
            #print s[:y] + s[x:]
            allFragments.append( (s[:y] + s[x:]) )
        
        x = (x + 1) % (len(s))
        y = (y + 1) % (len(s))
    allPossibleFragments(s, size - 1)
        
         

def getFile():
    from os.path import expanduser
    home = expanduser("~")
    #fileName = raw_input("File name: ")
    #fileName = "theoretical_spectrum_data.txt"
    fileName = "dataset_20_3.txt"
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
    allPossibleFragments(seq, len(seq))
    
    print allFragments
    
    for a in allFragments:
        #print a
        spectrum.append( AAtoWeight(a) )
    
    
    spectrum.sort(cmp=None, key=None, reverse=False)
    spec = ''
    
    for sp in spectrum:
        spec += str(sp) + " "
        
    print spec
        
    
    #f.readline()
    #pattern = f.readline()
    
    
    
    
    
    
    
    
    
    