'''
Created on Nov 13, 2013

@author: Mike
'''
import sys
sys.setrecursionlimit(10000)


class nucleoTree:
    def __init__(self, nucleotide):
        self.nuclotide = nucleotide
        self.children = []
        
    def addChild(self, obj):
        self.children.append(obj)
            
def buildTree(level, node):                
    if (level == 0):
        print node.children
        print len(node.children)
        return
    else:
        An = nucleoTree("A")
        node.addChild(An)
        buildTree(level - 1, An)
        Tn = nucleoTree("T")
        node.addChild(Tn)
        buildTree(level - 1, Tn)
        Cn = nucleoTree("C")
        node.addChild(Cn)
        buildTree(level - 1, Cn)
        Gn = nucleoTree("G")
        node.addChild(Gn)
        buildTree(level - 1, Gn)
        
def checkTree(node, kMer):
    if (len(node.children) == 0):
        return kMer + " "
    else:
        for x in node.children:
            kMer += x.nuclotide
            checkTree(node, kMer)
            return kMer
    


def getFile():
    from os.path import expanduser
    home = expanduser("~")
    #fileName = raw_input("File name: ")
    #fileName = "frequent_words_mismatch_data.txt"
    fileName = "dataset_8_4.txt"  #AAAACCCCCC ACACCCCAAA ACCCCCCGCA CCCTCGCATA 
    #fileName = ""
    path = home + '//Downloads//' + fileName 
    # print path
    fileToOpen = open(path , 'r')
    return fileToOpen

if __name__ == '__main__':
    f = getFile()
    #f.readline()
    seq = str(f.readline())
    k = int(f.readline())
    mis = int(f.readline())
    #pattern = "ATTCTGGA"
    #seq = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
    #mis = 3
    
    root = nucleoTree("root")
    buildTree(3, root)
    stringTree = ""
    stringTree = checkTree(root, stringTree)
    print stringTree

    
    
    #allKmers(k, "")
    #print len(kMerArray)
    #findKmers(seq, k, mis)
    #result = findMostFrequent(kMerArray)
    #print result
    
    
    
    
    
    
    