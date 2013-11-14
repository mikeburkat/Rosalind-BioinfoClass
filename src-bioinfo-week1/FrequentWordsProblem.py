'''
Created on Nov 12, 2013

@author: Mike
'''

class kMer:
    def __init__(self, sequence, frequency):
        self.sequence = sequence
        self.frequency = frequency + 1
    def addOne(self):
        self.frequency += 1


def findKmers(s, k):
    i = 0
    j = k
    
    ini = kMer("A", 0)
    array = [ini]
    while (j < len(s)):
        temp = kMer(s[i:j], 0)
        t = 0
        while (t < len(array)):
            if (temp.sequence == array[t].sequence):
                array[t].addOne()
                
            t += 1
        array.append(temp)
        i += 1
        j += 1
    return array
    
def findMostFrequent(a):
    max = 0
    kmers = ""
    for x in a:
        if ( max < x.frequency):
            max = x.frequency
    for x in a:
        if (max == x.frequency):
            kmers = kmers + x.sequence + " "
    return kmers

if __name__ == '__main__':
    seq = raw_input("DNA sequence: ")
    k = int(raw_input("k-mer: "))
    all = findKmers(seq, k)
    result = findMostFrequent(all)
    print result
    
    