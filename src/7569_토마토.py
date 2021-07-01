from collections import deque
import sys
input = sys.stdin.readline
m, n, h = map(int, input().rstrip().split())
q = deque()
num_t = 0
cnt = 0
wh = []
mx = [1, 0, -1, 0, 0, 0]
my = [0, 1, 0, -1, 0, 0]
mz = [0, 0, 0, 0, 1, -1]
for i in range(h):
	wh.append([])
	for j in range(n):
		wh[i].append(list(map(int,input().rstrip().split())))
		for k, t in enumerate(wh[i][j]):
			if t == 1:
				q.append((i, j, k))
			if t == 0:
				num_t += 1
if num_t == 0:
	print(0)
	sys.exit()
while q:
	z, y, x = q.popleft()
	if cnt < wh[z][y][x]:
			cnt = wh[z][y][x]
	for i in range(6):
		tx, ty, tz = x+mx[i], y+my[i], z+mz[i]
		if 0<=tx<m and 0<=ty<n and 0<=tz<h and wh[tz][ty][tx] == 0:
			q.append((tz, ty, tx))
			wh[tz][ty][tx] = wh[z][y][x] + 1
			num_t -= 1
if num_t:
	print(-1)
else:
	print(cnt-1)