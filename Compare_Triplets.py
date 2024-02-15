l=list(map(int,input().split()))
l1=list(map(int,input().split()))
b=0
a=0
for i in range(3):
    if l[i]==l1[i]:
        b=b+0
        a=a+0
    elif l[i]>l1[i]:
        a+=1
    else:
        b+=1
print("%d %d"%(a,b))