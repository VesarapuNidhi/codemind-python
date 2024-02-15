t=int(input())
for j in range(t):
    a,b=map(int,input().split())
    m=[]
    l=list(map(int,input().split()))
    l1=list(map(int,input().split()))
    for i in range(a):
        m.append(l[i])
    for i in range(b):
        m.append(l1[i])
    print(*sorted(m))