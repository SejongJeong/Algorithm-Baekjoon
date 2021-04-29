from itertools import combinations
import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
c = combinations(range(1,n+1),m)
for i in c:
    print(*i)