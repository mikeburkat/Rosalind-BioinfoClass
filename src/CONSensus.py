'''
Created on Oct 6, 2013

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

def seperateFASTA(multiLines):
    sequences_FASTA = {}
    for line in multiLines:
        if line.startswith('>'):
            name = line[1:].rstrip('\n')
            sequences_FASTA[name] = ''
        else :
            sequences_FASTA[name] += line.rstrip('\n').rstrip('*')

    return sequences_FASTA

def bpFrequency(seqs):
    baseSeqs = []
    notBase = 0
    
    for key in seqs:
        baseSeqs.append(seqs[key])
    
    freq =  [ [0 for i in range(4)] for j in range(len(baseSeqs[0]))]
    
    for s in baseSeqs:
        length = 0
        for c in s:
            if c == 'A':
                freq[length][0] += 1
                length += 1
            elif c == 'C':
                freq[length][1] += 1
                length += 1
            elif c == 'G':
                freq[length][2] += 1
                length += 1
            elif c == 'T':
                freq[length][3] += 1    
                length += 1
            else:
                notBase =+ 1
    return freq


def getConsensus(bps):
    con = ''
    for x in bps:
        if (x[0] >= x[1] and x[0] >= x[2] and x[0] >= x[3]):
            con += 'A'
        elif (x[1] >= x[0] and x[1] >= x[2] and x[1] >= x[3]):
            con += 'C'
        elif (x[2] >= x[0] and x[2] >= x[1] and x[2] >= x[3]):
            con += 'G'
        elif (x[3] >= x[0] and x[3] >= x[1] and x[3] >= x[2]):
            con += 'T'
    return con


def getProfile(pr):
    A = 'A: '
    C = 'C: '
    G = 'G: '
    T = 'T: '
    for x in pr:
        A += str(x[0]) + ' '
        C += str(x[1]) + ' '
        G += str(x[2]) + ' '
        T += str(x[3]) + ' ' 
            
            
    return A + '\n' + C + '\n' + G + '\n' + T

if __name__ == '__main__':
    f = getFile()
    allLines = f.readlines()
    motif = f.readline()
    f.close()
    sequences = seperateFASTA(allLines)
    bpProfile = bpFrequency(sequences)
    
    consensus = getConsensus(bpProfile)
    profile = getProfile(bpProfile)
    
    print consensus
    print profile
    
    
    