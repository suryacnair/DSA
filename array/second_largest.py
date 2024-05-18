def second(n):
    large=0
    sec=-1
    for i in range(1,len(n)):
        if(n[i]>n[large]):
            sec=large
            large=i
        elif(n[i]!=n[large]):
            if(n[i]>n[sec] or sec==-1):
                sec=i
    return sec        
          


n=[20,10,20,10 ]
print(second(n))