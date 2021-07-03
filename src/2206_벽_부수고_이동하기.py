from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
mp = [list(input().rstrip()) for _ in range(n)]
mx = [1, 0, -1, 0]
my = [0, 1, 0, -1]
q = deque()
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
q.append((0, 0, 1))
visited[0][0][1] = 1
min_num = 0
while q:
	y, x, isbreak = q.popleft()
	if x == m-1 and y == n-1:
		min_num = visited[y][x][isbreak]
		break
	for i in range(4):
		tx, ty = x+mx[i], y+my[i]
		if 0<=tx<m and 0<=ty<n:
			if isbreak == 1 and mp[ty][tx] == '1':
				q.append((ty, tx, 0))
				visited[ty][tx][0] = visited[y][x][1] + 1
			elif mp[ty][tx] == '0' and visited[ty][tx][isbreak] == 0:
				q.append((ty, tx, isbreak))
				visited[ty][tx][isbreak] = visited[y][x][isbreak] + 1
if min_num:
	print(min_num)
else:
	print(-1)


# First Try - 시간 초과

# from collections import deque
# from copy import deepcopy
# n, m = map(int, input().split())

# mp = []
# mx = [1, 0, -1, 0]
# my = [0, 1, 0, -1]
# q = deque()
# onelist = []
# min_cnt = m*n
# for i in range(n):
# 	mp.append(list(input()))
# 	for j in range(m):
# 		if mp[i][j] == '1':
# 			onelist.append((i, j))
# for a, b in onelist:
# 	tm = deepcopy(mp)
# 	reach = False
# 	tm[a][b] = '0'
# 	q.append((0,0))
# 	tm[0][0] = '1'
# 	cnt = 0
# 	while q:
# 		len_q = len(q)
# 		cnt += 1
# 		for _ in range(len_q):
# 			y, x = q.popleft()
# 			if x == m-1 and y == n-1:
# 				reach = True
# 				break
# 			for i in range(4):
# 				tx, ty = x + mx[i], y + my[i]
# 				if 0<=tx<m and 0<=ty<n and tm[ty][tx] == '0':
# 					q.append((ty, tx))
# 					tm[ty][tx] = '1'
# 	if reach:
# 		min_cnt = min(cnt, min_cnt)
# if min_cnt == m*n:
# 	print(-1)
# else:
# 	print(min_cnt)