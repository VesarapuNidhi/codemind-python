n=int(input())
c=0
l=list(map(int,input().strip().split()))
for i in range(n):
    if l[i]%2!=0:
        c+=1
if c<=2:
    print("YES")
else:
    print("NO")