'''
Created on Nov 12, 2013

@author: Mike
'''

def rabbits(n, k):
    if (n < 1):
        return 0 
    elif (n < 2):
        return 1
    else:
        return rabbits(n-1, k) + rabbits(n-2, k) * k 


if __name__ == '__main__':
    n = int(raw_input("Enter months: "))
    k = int(raw_input("Enter rabbit pairs: "))
    rab = rabbits(n, k)
    print rab