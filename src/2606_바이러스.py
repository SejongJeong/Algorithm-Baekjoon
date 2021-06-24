import sys
input = sys.stdin.readline
number_of_computer = int(input())
graph = [[] for _ in range(number_of_computer+1)]
visited = [0 for _ in range(number_of_computer+1)]
number_of_edge = int(input())
for _ in range(number_of_edge):
	i, j = map(int, input().rstrip().split())
	graph[i].append(j)
	graph[j].append(i)
stack = list()
stack.append(1)
while stack:
	node = stack.pop()
	visited[node] = 1
	for next_node in graph[node]:
		if not visited[next_node]:
			stack.append(next_node)
print(sum(visited)-1)