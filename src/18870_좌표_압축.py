N = int(input())
numbers = list(map(int, input().split()))
arr = [(numbers[i], i) for i in range(N)]
arr.sort(key=lambda x: x[0])
coor = ['' for _ in range(N)]
cnt = 0
coor[arr[0][1]] = str(cnt)
for i in range(1, N):
	if arr[i-1][0] != arr[i][0]:
		cnt += 1
	coor[arr[i][1]] = str(cnt)
print(' '.join(coor))