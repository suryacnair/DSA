def dup(n):
    res=1
    for i in range(0,len(n)-1):
        if(n[i]!=n[res-1]):
                
                
                n[res]=n[i]
                res=res+1
                
    return res

n=[10,20,20,30,30,30]
print(dup(n))