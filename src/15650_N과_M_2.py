import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
visit = [False] * n
result = []
num = 0
def dfs(cnt):
    global num
    if cnt == m:
        print(*result)
        return
    for i in range(n):
        if visit[i] == True:
            continue
        if i < num:
            continue
        visit[i] = True
        result.append(i+1)
        num = i
        dfs(cnt+1)
        visit[i] = False
        result.pop()
        if len(result) > 0:
            num = result[-1] - 1
        else:
            num = 0
dfs(0)
