'''
Created on Dec 8, 2013

@author: Mike
'''

class EularianCycle:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.graph = []
        self.dataSet = "dataset_57_5.txt"
        #self.testSet = "eulerian_path.txt"
        self.testSet = "pair_end.txt"
        self.graphDic = {}
        self.d = 0
        
    
    
    def printResult(self, r):
        #print r
        s = ''
        temp = r[0].split("|")
        #print temp
        L = len(temp[0])
        d = self.d
        s += temp[0] + "_" * (self.d + 1) + temp[1]
        x = 1
        
        while x < len(r):
            #print s
            temp = r[x].split("|")
            #print temp[0][-1]
            s = s[:x+L-1] + temp[0][-1] + s[x+L:] + temp[1][-1]
            x += 1
            
            #if x == 205:
                #break
        
        print len(s)
        print s
    
    
    
    def removeExtraNode(self, node, cycle):    
        x = 0
        
        while x < len(cycle):
            #print cycle[x-1], cycle[x]
            if cycle[x-1] == node[0] and cycle[x] == node[1]:
                break
            x += 1 
        
        linearized = cycle[x:-1] + cycle[:x]
        #print x, cycle[x:-1] , cycle[:x]
        return linearized
    
        
    def addToGraph(self, node, graph):    
        
        if node[0] in graph:
            graph[node[0]].append(node[1])
            
        else:
            graph[node[0]] = [node[1]]
        
        return graph
        
    def findUnbalenced(self, nodes):
        missing = ''
        inOUT = {}
        
        for key in nodes:
            
            if key in inOUT:
                inOUT[key][1] = len(nodes[key])
                
            else:
                inOUT[key] = [0, len(nodes[key])]
            
            
            for k in nodes[key]:
                if k in inOUT:
                    inOUT[k][0] += 1
                else:
                    inOUT[k] = [1, 0]
        
        #print inOUT
        
        kIN = ''
        kOUT = ''
        for key in inOUT:
            if inOUT[key][0] > inOUT[key][1]:
                kIN = key 
                #print key, inOUT[key][0], inOUT[key][1]
            elif inOUT[key][0] < inOUT[key][1]:
                kOUT = key
                #print key, inOUT[key][0], inOUT[key][1]
        
        
        
        #print kIN, kOUT
        missing = [kIN, kOUT]
        return missing
            
    def reverseCycle(self, cycle):
        revCycle = []
        #print cycle
        for c in cycle:
            revCycle.insert(0, c)
        #print revCycle
        return revCycle
        
    def removeNode(self, key, nodes):
        
        #print nodes[key]
        if len(nodes[key]) > 1:
            nodes[key].pop(0)
        else:
            del nodes[key]
        
    
        return nodes
        
    def cycle(self, gD):
        import random
        from copy import deepcopy
        
        tempDic = deepcopy(gD)
        stack = []
        top = 0
        
        cycle = []
        
        
        #print tempDic
        stack.append(random.choice(tempDic.keys()))
        stack.append(tempDic[stack[top]][0])
        self.removeNode(stack[top], tempDic)
        top += 1
        
        while len(stack) > 0:
            #print "stack:", stack
            #print "cycle:", cycle
            
            if stack[top] in tempDic.keys():
                stack.append(tempDic[stack[top]][0])
                #print tempDic[stack[top]][0]
                
                
                '''mark as visited'''
                self.removeNode(stack[top], tempDic)
                top += 1
            else:
                cycle.append( stack[top] )
                stack.pop(top)
                top -= 1
                
        cycle = self.reverseCycle(cycle)
        return cycle
    
    
    def getPreSuf(self, pair):
        preSuf = []
        
        pS = pair.split("|")
        
        preSuf.append(pS[0][:-1] +"|"+ pS[1][:-1])
        preSuf.append(pS[0][1:] +"|"+ pS[1][1:])
        
        return preSuf
         
    def nodesToDic(self, graph):       
            graphDic = {}
            
            for g in graph:
                temp = self.getPreSuf(g)
                #print g, temp
                graphDic[temp[0]] = [temp[1]]
            
            return graphDic
            
            
            
            
    def read(self, f):
        d = f.readline()
        self.d = int(d)
         
        lines = f.readlines()
        
        for l in lines:
            if l == "Output:\n":
                break
            self.graph.append(l.rstrip('\n'))
            '''
            self.d = 2
            self.graph = ['GAGA|TTGA',
                          'TCGT|GATG',
                          'CGTG|ATGT',
                          'TGGT|TGAG',
                          'GTGA|TGTT',
                          'GTGG|GTGA',
                          'TGAG|GTTG',
                          'GGTC|GAGA',
                          'GTCG|AGAT']
            '''
            
    def printVAR(self):
        s = ''
        s += "Node List:" + "\n"
        for d in self.graph:
            s += d + "\n"
        return s

    def getFileName(self, test):
        if test:
            return self.testSet
        else:
            return self.dataSet

    def autoRun(self, f):
        self.read(f)
        #print self.printVAR()
        
        self.graphDic = self.nodesToDic(self.graph)
        
        #print len(self.graphDic), self.graphDic
        
        node = self.findUnbalenced(self.graphDic)
        self.graphDic = self.addToGraph(node, self.graphDic)
        
        result = self.cycle(self.graphDic)
        result = self.removeExtraNode(node, result)
        self.printResult(result)
        
        #s = ''
        #for r in result:
        #    s += r + '->'
        #print s[:-2]
        
def getFile(fileName):
    from os.path import expanduser
    home = expanduser("~")
    path = home + '//Downloads//' + fileName 
    #print path
    fileToOpen = open(path , 'r')
    return fileToOpen
       
if __name__ == '__main__':
    ec = EularianCycle()
    test = True
#     test = False
    f = getFile(ec.getFileName(test))    
    if test:
        f.readline()
    
    ec.autoRun(f)    
        