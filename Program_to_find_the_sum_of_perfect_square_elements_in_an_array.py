n=int(input())
s=0
l=list(map(int,input().split()))
for i in range(n):
    for j in range(0,l[i]+1):
        if j*j==l[i]:
            s+=l[i]
print(s)