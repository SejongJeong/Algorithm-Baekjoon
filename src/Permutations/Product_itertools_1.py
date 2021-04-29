from itertools import product
import sys
input = sys.stdin.readline
n,m = map(int, input().rstrip().split())
P = product(range(1,n+1),repeat = m)
for i in P:
    print(*i)
