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
        self.dataSet = "dataset_57_5 (1).txt"
        #self.testSet = "eulerian_path.txt"
        self.testSet = "str_recon.txt"
        self.graphDic = {}
        
        
    
    
    def printResult(self, r):
        
        s = ''
        s += r[0]
        x = 1
        while x < len(r):
            
            s += r[x][-1:]
            x += 1
        
        print s
    
    
    
    def removeExtraNode(self, node, cycle):    
        x = 0
        
        while x < len(cycle):
            print cycle[x-1], cycle[x]
            if cycle[x-1] == node[0] and cycle[x] == node[1]:
                break
            x += 1 
        
        linearized = cycle[x:-1] + cycle[:x]
        print x, cycle[x:-1] , cycle[:x]
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
        
        print inOUT
        
        kIN = ''
        kOUT = ''
        for key in inOUT:
            if inOUT[key][0] > inOUT[key][1]:
                kIN = key 
                print key, inOUT[key][0], inOUT[key][1]
            elif inOUT[key][0] < inOUT[key][1]:
                kOUT = key
                print key, inOUT[key][0], inOUT[key][1]
        
        
        
        print kIN, kOUT
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
        
        print nodes[key]
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
         
    def nodesToDic(self, graph):       
            graphDic = {}
            
            for g in graph:
                temp = g.split(" -> ")
                graphDic[temp[0]] = temp[1].split(",")
            
            return graphDic
            
            
    def read(self, f):
        lines = f.readlines()
        
        for l in lines:
            if l == "Output\n":
                break
            self.graph.append(l.rstrip('\n'))
            '''
        self.graph = [ "0 -> 2",
     "1 -> 3",
     "2 -> 1",
     "3 -> 0,4",
     "6 -> 3,7",
     "7 -> 8",
     "8 -> 9",
     "9 -> 6"]
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
        print self.printVAR()
        
        self.graphDic = self.nodesToDic(self.graph)
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
    #test = False
    f = getFile(ec.getFileName(test))    
    if test:
        f.readline()
    
    ec.autoRun(f)    
        