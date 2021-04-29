from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
CWR = combinations_with_replacement(range(1, n+1), m)
for i in CWR:
    print(*i)