import sys
input = sys.stdin.readline
n = int(input())
column = [0 for _ in range(n)]
result = 0
def queen(row):
    for i in range(row):
        if column[row] == column[i] or abs(column[row] - column[i]) == row - i:
            return False
    return True
def dfs(row):
    global result
    if  row == n:
        result += 1
        return
    for i in range(n):
        column[row] = i
        if queen(row):
            dfs(row+1)
dfs(0)
print(result)
