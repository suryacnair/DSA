def rev(n):
    for i in range(0,int(len(n)/2)):
        temp=n[i]
        n[i]=n[len(n)-1-i]
        n[len(n)-1-i]=temp
    return n
n=[30,20,5,8]
print(rev(n))