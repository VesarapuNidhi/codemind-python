n=int(input())
l=list(map(int,input().strip().split()))
for i in range(n):
    pro=1
    for j in range(n):
        if i!=j:
            pro*=l[j]
    print(pro,end=' ')