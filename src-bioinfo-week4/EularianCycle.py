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
        self.dataSet = "dataset_57_2 (2).txt"
        self.testSet = "eulerian_cycle.txt"
        self.graphDic = {}
            
    def reverseCycle(self, cycle):
        revCycle = []
        #print cycle
        for c in cycle:
            revCycle.insert(0, c)
        #print revCycle
        return revCycle
        
    def removeNode(self, key, nodes):
        
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
            
        #self.graph = ["0 -> 3","1 -> 0", "2 -> 1,6","3 -> 2", "4 -> 2", "5 -> 4", "6 -> 5,8", "7 -> 9",   "8 -> 7", "9 -> 6"]
            
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
        result = self.cycle(self.graphDic)
        s = ''
        for r in result:
            s += r + '->'
        print s[:-2]
        
def getFile(fileName):
    from os.path import expanduser
    home = expanduser("~")
    path = home + '//Downloads//' + fileName 
    #print path
    fileToOpen = open(path , 'r')
    return fileToOpen
       
if __name__ == '__main__':
    ec = EularianCycle()
    #test = True
    test = False
    f = getFile(ec.getFileName(test))    
    if test:
        f.readline()
    
    ec.autoRun(f)    
        