x=int(input())
f=1
i=0
for i in range(1,x+1):
    a=int(input())
    for j in range(1,a+1):
        f*=j
    print(f)
    f=1