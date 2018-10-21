from math import sqrt, floor, ceil
from collections import Counter

with open('primes-to-100k.txt', 'r') as infile:
    data=infile.read().splitlines()
    infile.close()

primes=[int(d) for d in data]

def fun_2(n):
    list_of_n=[]
    sq=int(floor(sqrt(n)/2)+1)
    row=int(ceil(n/2))
    for m in range(2, sq):
        o=1
        U=0
        while True:
            U=(2*m-1)**2+2*o*(2*m-1)
            if U<=n:
                o+=1
                list_of_n.append(U)
            else:
                break
    return list_of_n

def fun_1(n):
    
    pcf=0
    pi1,pi2,pi3=[],[],[]
    
    for x in range(n):
        if x in primes:
            pcf+=1

    sq=floor(sqrt(n))

    z1 = float(n-1)/2.0
    z2 = 0.0
    for l in range(2, ((int(sq)+1)/2)+1):
        s=float(n-(2*l-1)**2)/float(2*(2*l-1))
        z2+=s

    z3=((float(sq)+1.0)/2.0)-2.0

    res=z1-z2-z3
    rep=0
    for k, v in Counter(fun_2(n)).iteritems():
        if v>1:
            rep+=v-1
            
    return pcf, res+rep, res

for x in range(5):
    print fun_1(10**x)

     
    

    
