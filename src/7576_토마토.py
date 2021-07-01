from collections import deque
m, n = map(int, input().split())
wh = [list(input().split()) for _ in range(n)]
q = deque()
mx = [1, 0, -1, 0]
my = [0, 1, 0, -1]
for i in range(n):
	for j in range(m):
		if wh[i][j] == '1':
			q.append((i, j, 0))
			wh[i][j] = '-1'
store_t = 0
while q:
	y, x, t = q.popleft()
	if store_t < t:
		store_t = t
	for k in range(4):
		tx, ty = x+mx[k], y+my[k]
		if 0<=tx<m and 0<=ty<n and wh[ty][tx] == '0':
			q.append((ty, tx, t+1))
			wh[ty][tx] = '-1'
for i in range(n):
	for j in range(m):
		if wh[i][j] == '0':
			print(-1)
			exit()
print(max(0, store_t))