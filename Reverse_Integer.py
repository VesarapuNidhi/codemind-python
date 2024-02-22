x=int(input())
r=0
sum=0
if x<0:
    x=-x
    while x!=0:
        r=x%10
        sum=sum*10+r
        x=x//10
    print(-sum)
else:
    while x!=0:
        r=x%10
        sum=sum*10+r
        x=x//10
    print(sum)