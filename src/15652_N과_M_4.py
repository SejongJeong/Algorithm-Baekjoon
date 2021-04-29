import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
num = 0
result = []
def dfs(cnt):
    global num
    if cnt == m:
        print(*result)
        return
    for i in range(n):
        if num > i:
            continue
        num = i
        result.append(i+1)
        dfs(cnt+1)
        result.pop()
        if len(result) == 0:
            num = 0
        else:
            num = result[-1] -1
dfs(0)