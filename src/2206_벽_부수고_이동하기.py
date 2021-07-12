from collections import deque
n, m = map(int, input().split())
m = []
one = []
mx = [1, 0, -1, 0]
my = [0, 1, 0, -1]
for i in range(n):
	m.append(list(input()))
	for j in range(m):
		if m[i][j] == '1':
			one.append((i,j))
min_cnt = n*m
check_av = False
for a, b in one:
	tm = m
	tm[a][b] = '0'
	cnt = 0
	q = deque()
	q.append((0,0))
	tm[0][0] = '1'
	reach = False
	while q:
		len_q = len(q)
		for _ in range(len_q):
			y, x = q.popleft()
			if x == m-1 and y == n-1:
				reach = True
				break
			for i in range(4):
				tx, ty = x+mx[i], y+my[i]
				if 0<=tx<m and 0<=ty<n and tm[ty][tx] == '0':
					q.append((ty, tx))
					tm[ty][tx] = '1'
		if reach:
			check_av = True
			break
		cnt += 1
	min_cnt = min(cnt, min_cnt)
if check_av:
	print(min_cnt)
else:
	print(-1)
