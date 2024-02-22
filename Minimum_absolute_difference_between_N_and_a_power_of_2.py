import math
def minAbsDiff(n):
    left=1<<(int)(math.floor(math.log2(n)))
    right=left*2
    return min((n-left),(right-n))
if __name__=='__main__':
    n=int(input())
    print(minAbsDiff(n))