import sys
input = sys.stdin.readline
n = int(input())
check = [[False for _ in range(n)] for _ in range(n)]
def dfs(x):
    global check
    if x == n:
        return 1
    cnt = 0
    for i in range(n):
        if valid(x, i):
            check[i][x] = True
            cnt += dfs(x+1)
            check[i][x] = False
    return cnt
def valid(x,y):
    global check
    print("valid x, y : ", x,y)
    diff = 0
    for j in range(x-1, -1, -1):
        diff += 1
        print("j, diff :", j, diff)
        if check[y][j] or (y-diff >= 0 and check[y-diff][j]) or (y+diff < n and check[y+diff][j]):
            print("false", check[y][j], y-diff >= 0 and check[y-diff][j],y+diff < n and check[y+diff][j])
            return False
    return True
print(dfs(0))
