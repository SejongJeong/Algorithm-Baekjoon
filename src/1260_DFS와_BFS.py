from collections import deque
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
	i, j = map(int, input().split())
	graph[i].append(j)
	graph[j].append(i)
for sublist in graph:
	sublist.sort()
dfs = []
dfs_check = [1 for _ in range(n+1)]
dfs.append(v)
while dfs:
	tmp = dfs.pop()
	if dfs_check[tmp]:
		print(tmp, end=' ')
		dfs_check[tmp] = 0
		dfs += reversed(graph[tmp])
print()
bfs = deque()
bfs_check = [1 for _ in range(n+1)]
bfs.append(v)
while bfs:
	tmp = bfs.popleft()
	if bfs_check[tmp]:
		print(tmp, end=' ')
		bfs_check[tmp] = 0
		bfs.extend(deque(graph[tmp]))
print()