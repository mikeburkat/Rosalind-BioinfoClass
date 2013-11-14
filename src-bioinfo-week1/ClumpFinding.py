'''
Created on Nov 13, 2013

@author: Mike
'''

class kMer:
    
    def __init__(self, sequence, frequency, position):
        self.sequence = sequence
        self.frequency = frequency + 1
        self.positions = [position]
    
    def addOnePosition(self, position):
        self.frequency += 1
        self.positions.append(position)
        






def findKmers(s, k):
    i = 0
    j = k
    
    ini = kMer("A", 0, 0)
    array = [ini]
    while (j < len(s)):
        temp = kMer(s[i:j], 0, j)
        t = 0
        found = False
        while (t < len(array)):
            if (temp.sequence == array[t].sequence):
                array[t].addOnePosition(i)
                #print array[t].positions
                #print array[t].sequence
                found = True
            
            t += 1
        if (not found):
            array.append(temp)
        i += 1
        j += 1
    return array


def check(array, search):
    found = False
    for x in array:
        if (x == search):
            found = True
            break
    return found


def findClumps(a, L, t):
    r = []
    for x in a:
        if ( t <= x.frequency):
#             print x.positions
            i = 0
            while (i + t < len(x.positions)):
                if ( x.positions[i+t] - x.positions[i] <= L ):
                    if(not check(r, x.sequence)):
                        r.append(x.sequence)
                i += 1
    return r


def getFile():
    from os.path import expanduser
    home = expanduser("~")
        
    fileName = raw_input("File name: ")
    path = home + '//Downloads//' + fileName 
    # print path
    fileToOpen = open(path , 'r')
    return fileToOpen

if __name__ == '__main__':
    f = getFile()
    #f.readline()
    seq = str(f.readline())
    ls = f.readline()
    print seq
    kLt = ls.split()
    f.close()
    allKmers = findKmers(seq, int(kLt[0]))
    
    result = findClumps(allKmers, int(kLt[1]), int(kLt[2]))
    for x in result:
        print x
