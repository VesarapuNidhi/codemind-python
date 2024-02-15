n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(n):
    if l[i]==0:
        a.append(l[i])
for i in range(n):
    if l[i]==1:
        a.append(l[i])
print(*a)