N = int(input())
s_map = []
for _ in range(N):
	s_map.append(input())
visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
	for j in range(N):