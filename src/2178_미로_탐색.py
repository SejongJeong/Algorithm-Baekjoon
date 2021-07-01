from collections import deque
n, m =  map(int, input().split())
maze = [list(input()) for _ in range(n)]
mx = [1, 0, -1, 0]
my = [0, 1, 0, -1]
q = deque()
q.append((0,0,1))
maze[0][0] = "0"
cnt = 0
while q:
	x, y, t = q.popleft()
	if x == m - 1 and y == n -1:
		cnt = t
		break
	for i in range(4):
		t_x, t_y = x + mx[i], y + my[i]
		if 0 <= t_x < m and 0 <= t_y < n and maze[t_y][t_x] == "1":
			q.append((t_x, t_y, t+1))
			maze[t_y][t_x] = "0"
print(cnt)