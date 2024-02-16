a=int(input())
b=int(input())
s=0
for i in range(a,b+1):
  s=i
  sum=0
  while i!=0:
   r=i%10
   sum=sum*10+r
   i=i//10
  if sum==s:
      print(s,end=' ')