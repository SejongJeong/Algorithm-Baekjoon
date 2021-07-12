n = int(input())
conference = [tuple(map(int, input().split())) for _ in range(n)]
conference.sort(key=lambda x: (x[1],x[0]))
cnt = 0
end = 0
for a,b in conference:
	if a>=end:
		cnt += 1
		end = b
print(cnt)