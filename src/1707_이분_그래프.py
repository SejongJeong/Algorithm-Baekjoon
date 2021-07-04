from collections import deque
import sys
input = sys.stdin.readline
tc = int(input())
q = deque()
for _ in range(tc):
	v, e = map(int, input().rstrip().split())
	g = [set() for _ in range(v+1)]
	visited = set()
	cnt = 1
	check = False
	bi = [set(),set()]
	for _ in range(e):
		e1, e2 = map(int, input().rstrip().split())
		g[e1].add(e2)
		g[e2].add(e1)
	q.append(1)
	visited.add(1)
	bi[cnt%2].add(1)
	while q:
		len_q = len(q)
		cnt += 1
		for _ in range(len_q):
			tmp = q.popleft()
			for nv in g[tmp]:
				if nv not in visited:
					q.append(nv)
					visited.add(nv)
					bi[cnt%2].add(nv)
				else:
					if nv in bi[(cnt+1)%2]:
						check = True
						break
			if check:
				break
		if check:
			break
	if check:
		print("NO")
	else:
		print("YES")