'''
Created on Oct 7, 2013

@author: Mike
'''

import sys
import copy


def getFile():
    from os.path import expanduser
    home = expanduser("~")
        
    fileName = raw_input("File name: ")
    path = home + '//Desktop//Rosalind//' + fileName 
    
    fileToOpen = open(path , 'r')
    return fileToOpen

def seperateFASTA(multiLines):
    sequences_FASTA = {}
    for line in multiLines:
        if line.startswith('>'):
            name = line[1:].rstrip('\n')
            sequences_FASTA[name] = ''
        else :
            sequences_FASTA[name] += line.rstrip('\n').rstrip('*')

    return sequences_FASTA

def findShortest(seqs):
    
    keyShrt = seqs.keys()[0]
    
    for key in seqs:
        if (len(seqs[key]) < len(seqs[keyShrt])):
            keyShrt = key
    return keyShrt


def findLongestSubstring(sKey, ss):
    t = 0
    k = len(ss[sKey])
    sbs = ss[sKey]
    print (len(ss)-1)
    
    while len(sbs) > 0:
        sbs = ss[sKey][t:k]
        
        x = t
        y = k
        
        while y < len(ss[sKey]):
            sbs = ss[sKey][x:y]
            found = 0
            
            
            
            for key in ss:
                i = 0
                j = k
                if (key != sKey):
                    i = 0
                    j = k
                    #print k
                    while j < len(ss[key]):
                        
                           
                        
                        print sbs
                        print ss[key][i:j]
                    
                        if (sbs == ss[key][i:j]):
                            found += 1
                            print sbs
                            print key
                            print ss[key][i:j]
                            print 'found %i' % (found)
                            
                            
                            if (found == (len(ss)-1)):
                                return sbs  
                            
                            break
                            
                                
                        
                        i += 1
                        j += 1
                    if (found == 0):
                        break
                    
            x += 1
            y += 1
        
        
        
        k = k - 1
        
        
        
def checkALL(sb, toCheck):
    j = 0
    k = len(sb)
    toCheck = copy.deepcopy(toCheck)
    
    if (len(toCheck) == 0):
        return True
    
    key = toCheck.keys()[0]
    #print key
    #print len(toCheck)
    
    
    while k < len(toCheck[key]):
        
        if (len(toCheck) < 2):
            print key
            print len(toCheck)
            print sb
            print toCheck[key][j:k]
        
        
        if (sb == toCheck[key][j:k]):
            
            del toCheck[key]
            isIt = checkALL(sb, toCheck)
            if isIt:
                return True
                break
            else:
                return False
                break
        else:
            j += 1
            k += 1
    
    return False
    
            
                    
        
            


def fLS(sbs, left):
    #print sbs
    #if (len(left) == 0):
    #    return sbs
    
    
    y = len(sbs) - 1
    s = sbs
    stillLeft = copy.deepcopy(left)
    
    while len(s) > 0:
        x = y
        p = 0
        
        while x < len(sbs):
            
            s = sbs[p:x]
            
            print len(s) , s
            
            if checkALL(s, stillLeft):
                return s
            p += 1
            x += 1
        
        
        y -= 1
    
    
        
        
    
    
    
    
    
    #else :
        
        #del left[left.keys()[0]]
        #print len(left)
        #print left
        #fLS(sbs, left)
        
        
    
    
    return sbs





if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    f = getFile()
    allLines = f.readlines()
    f.close()
    sequences = seperateFASTA(allLines)
    #for key in sequences:
    #    print key
    #    print sequences[key]
    shortest = findShortest(sequences)
    motif = fLS(sequences[shortest], sequences)
    print 'done'
    print len(motif), motif
    #                        rosalind_lcsm.txt
    
    #
    
    
    