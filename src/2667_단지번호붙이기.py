from collections import deque
def bfs(i, j):
	global s_map
	global visited
	global number_of_house
	global N
	cnt = 0
	q = deque()
	q.append((i, j))
	visited[i][j] = True
	while q:
		a, b = q.popleft()
		cnt += 1
		if b+1<N and s_map[a][b+1] == "1" and not visited[a][b+1]:
			q.append((a, b+1))
			visited[a][b+1] = True
		if a+1<N and s_map[a+1][b] == "1" and not visited[a+1][b]:
			q.append((a+1, b))
			visited[a+1][b] = True
		if a-1>=0 and s_map[a-1][b] == "1" and not visited[a-1][b]:
			q.append((a-1, b))
			visited[a-1][b] = True
		if b-1>=0 and s_map[a][b-1] == "1" and not visited[a][b-1]:
			q.append((a, b-1))
			visited[a][b-1] = True
	number_of_house.append(cnt)

N = int(input())
s_map = []
for _ in range(N):
	s_map.append(input())
visited = [[False for _ in range(N)] for _ in range(N)]
number_of_house = []
for i in range(N):
	for j in range(N):
		if s_map[i][j] ==  "1" and not visited[i][j]:
			bfs(i, j)

number_of_house.sort()
print(len(number_of_house))
print('\n'.join(map(str, number_of_house)))