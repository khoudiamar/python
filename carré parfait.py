from math import *


def liste(l):
    p = []
    i, imax = 1, 2**len(l)-1
    while i <= imax:
        a = []
        j, jmax = 0, len(l)-1
        while j <= jmax:
            if (i>>j)&1 == 1:
                a.append(l[j])
            j += 1
        p.append(a)
        i += 1 
    return p       
       

def execute():
    n=int(input("Donner n: "))
    m=int(input("Donner m: "))
    l=[]
    while n <= m:
        l.append(n)
        n=n+1

    p=liste(l)
    c=0
    for i in range (len(p)):
        m=1
        for j in range (len(p[i])):
            m=m*p[i][j]
        if sqrt(m)== int(sqrt(m)):
            c=c+1
    print("C(n,m)=",c)
execute()    

  
  
 
