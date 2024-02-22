n=int(input())
sum=0
p=1
while n!=0:
 r=n%10
 sum=sum+r
 p=p*r
 n=n//10
if sum==p:
    print("Spy Number")
else:
    print("Not Spy Number")