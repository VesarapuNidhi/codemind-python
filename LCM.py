x,y=map(int,input().split())
for i in range(1,(x*y)+1):
    if i%x==0 and i%y==0:
        print(i)
        break