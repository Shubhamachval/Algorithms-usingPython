#intiallize array
ary=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0], 
     [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]] 

#check collision with other queen
def possible(row,col,n):
    for i in range(0,n):
        if ary[row][i]=='q' or ary[i][col]=='q':
            return False    
    r,c=row,col
    
    while r>=0 and c>=0:
        if ary[r][c]=='q':
            return False
        r-=1
        c-=1
        
    r,c=row,col    
    while r>=0 and c<n:
        if ary[r][c]=='q':
            return False
        r-=1
        c+=1
   
    return True

#backtracing method to place queen at right place
def queen(r,c,n):
    if c==n:
        return False
    else:
        while c<n:
            if possible(r,c,n):
                ary[r][c]='q'
                if r+1==n:
                    return True
                else:
                    if queen(r+1,0,n):
                        return True
                    else:
                        ary[r][c]=0
        
            c+=1 
 
#function calling           
queen(0,0,len(ary))

#print ary
for a in ary:
      print a
       


