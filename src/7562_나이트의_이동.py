from collections import deque
tc = int(input())
mx = [2, 1, -1, -2, -2, -1, 1, 2]
my = [1, 2, 2, 1, -1, -2, -2, -1]
for _ in range(tc):
	n = int(input())
	q = deque()
	m = [[False for _ in range(n)] for _ in range(n)]
	fy, fx = map(int, input().split())
	ry, rx = map(int, input().split())
	q.append((fy, fx))
	reach = False
	m[fy][fx] == True
	cnt = 0
	while q:
		len_q = len(q)
		for _ in range(len_q):
			y, x = q.popleft()
			if x == rx and y == ry:
				reach = True
				break
			for i in range(8):
				tx, ty = x + mx[i], y+my[i]
				if 0<=tx<n and 0<=ty<n and not m[ty][tx]:
					q.append((ty, tx))
					m[ty][tx] = True
		if reach:
			print(cnt)
			break
		cnt += 1