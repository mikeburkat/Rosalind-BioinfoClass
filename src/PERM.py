'''
Created on Oct 6, 2013

@author: Mike
'''
def perm(now, left, count):
    count += 1
    y = len(left)
    for x in range(y):
        print left[now]
        now += 1
        
        perm(now, left[now-1:y],count)
        x += 1
        
    
    
    
    
    return count

if __name__ == '__main__':
    k = int(raw_input("k: "))
    i = 1
    numList = ''
    while i <= k:
        numList += str(i)
        i += 1
    print numList
    permutations = perm(0, numList, 0)
    print permutations
    