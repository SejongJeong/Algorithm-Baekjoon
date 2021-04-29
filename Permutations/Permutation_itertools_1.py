import sys
from itertools import permutations
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
P = permutations(range(1, N+1), M)
for i in P:
    print(*i)