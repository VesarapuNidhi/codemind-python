n=int(input())
p='0123456789'
for i in range(n):
    k=input()
    for j in k:
        if j in p:
            print("Yes")
            break
    else:
        print("No")