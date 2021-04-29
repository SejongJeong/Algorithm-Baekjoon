import sys
input =  sys.stdin.readline
n,m = map(int, input().rstrip().split())
result = []
def dfs(cnt):
    if cnt == m:
        print(*result)
        return
    for i in range(n):
        result.append(i+1)
        dfs(cnt+1)
        result.pop()
dfs(0)