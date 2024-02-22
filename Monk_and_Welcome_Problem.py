def add_arrays(A, B):
    C = []  
    n = len(A)
    for i in range(n):
        C.append(A[i] + B[i])  
    return C
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = add_arrays(A, B)
print(*result)