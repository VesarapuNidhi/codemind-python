n=int(input())
s=0
arr=[]
for i in range(n):
    e=int(input())
    arr.append(e)
l=int(input())
for i in range(n):
    if arr[i]<=l:
        s+=1
    if arr[i]>l:
        s+=2
print(s)