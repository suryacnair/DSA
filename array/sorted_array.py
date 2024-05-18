def check(n):
    for i in range(0,len(n)-1):
        if(n[i]>n[i+1]):
            return False
    return True       


n=[10,10,0]
print(check(n))