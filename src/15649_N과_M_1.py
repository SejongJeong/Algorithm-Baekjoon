import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
visit = [False] * n
permutation = []
def dfs(cnt):
    if cnt == m:
        print(*permutation)
        return
    for i in range(n):
        if visit[i] == True:
            continue
        visit[i] = True
        permutation.append(i+1)
        dfs(cnt+1)
        permutation.pop()
        visit[i] = False

dfs(0)