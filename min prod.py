from math import log





def minProd(k):
    
    Total = 0  
    for i in range(2, k+1):
        p = float('inf')
        
        for j in range(1, int(log(i,2))+1 ):
            w = win(i, j)
            if w < p :
                p = w 

        Total += p

    print( "Somme de la longueur des chaines d'exponentiations =", Total )





def win(a, k):
    
    
    b = bin(a)[2:]
    b = b[::-1]
    L = len(b)-1
    

    pr= {1:2, 2:4}
    for i in range(1, 2**(k-1) ) :
        pr[2*i+1] = pr[2*i-1]*pr[2]
    
    m = len(pr) - 1 
    indx_utile, X, i = 1, 1, L

    
    while i >= 0 :
        if b[i] == '0':
            
            X = X**2
            m, i = m+1, i-1 

        else :
            f = []
            for j in range(k) :
                h = max(i-j,0)
                f.append( (b[h:i+1], h) ) if b[ h ] == '1' else None
            
            
            seq, l = sorted(f, key=lambda x: -len(x[0]) )[0]
            seq = int( seq[::-1], 2 )

            
            for _ in range(i-l+1):
                X = X**2
            m = m + (i-l+1) if X > 1 else m
            
            X = X*pr[ seq ]

            if indx_utile < pr[ seq ] :
                indx_utile = pr[ seq ]
            
            
            m = m + 1 if X > pr[ seq ]  else m
            i = l-1
    
    
    m = m - sum( i > indx_utile for i in pr.values() )
    return m
