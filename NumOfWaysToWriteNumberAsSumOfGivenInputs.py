def getWays(n,c):
    #creating array of n x c
    ary=[[-1]*(n+1)]*len(c) 
    #intialize first col with 1
    for i in range(0,len(c)):    
        ary[i][0]=1
    #use dynamic approach to get ways
    for i in range (0,len(c)):
        for j in range (1,n+1):
            #count number of ways for sum(j) possible with c(i)
            x=ary[i][j-c[i]] if j-c[i]>=0 else 0 
            #count number of ways for sum(j) possible without c(i)
            y=ary[i-1][j] if i>0 else 0
            #total ways of for sum possible with c(i) and its previous element c[i-1]
            ary[i][j]= x+y
    
    #return last col of last row which gives sum of all possible ways
    return ary[len(c)-1][n]

#example 
print(getWays(10000,[1,5]))   