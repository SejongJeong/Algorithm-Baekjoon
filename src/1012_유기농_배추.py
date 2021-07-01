from collections import deque
T = int(input())
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)
for _ in range(T):
	m, n, k = map(int, input().split())
	farm = [[False for _ in range(m)] for _ in range(n)]
	visited = [[False for _ in range(m)] for _ in range(n)]
	q = deque()
	for _ in range(k):
		j, i = map(int, input().split())
		farm[i][j] = True
	cnt = 0
	for y in range(n):
		for x in range(m):
			if farm[y][x] and not visited[y][x]:
				cnt += 1
				q.append((x, y))
				visited[y][x] = True
				while q:
					a, b = q.popleft()
					for k in range(4):
						t_x = a + dx[k]
						t_y = b + dy[k]
						if 0<=t_x<m and 0<=t_y<n and farm[t_y][t_x] and not visited[t_y][t_x]:
							q.append((t_x, t_y))
							visited[t_y][t_x] = True
	print(cnt)