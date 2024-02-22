n=int(input())
c=0
sum=0
f=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    while n!=0:
        r=n%10
        sum=sum*10+r
        n=n//10
    for i in range(1,sum+1):
        if sum%i==0:
            f+=1
    if f==2:
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")