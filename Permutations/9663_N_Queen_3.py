import sys
input = sys.stdin.readline
n = int(input())
result = 0
column, diagonal_left, diagonal_right  = [False for _ in range(n)], [False for _ in range(2*n-1)], [False for _ in range(2*n-1)]
def dfs(cnt):
    global result
    if cnt == n:
        result += 1
        return
    for i in range(n):
        if not(column[i] or diagonal_left[cnt+i] or diagonal_right[cnt-i+n-1]):
            column[i] = diagonal_left[cnt+i] = diagonal_right[cnt-i+n-1] = True
            dfs(cnt+1)
            column[i] = diagonal_left[cnt+i] = diagonal_right[cnt-i+n-1] = False
dfs(0)
print(result)

    