N = int(input())
num = N
cnt = 0
while True:
	str_num = str(num)
	list_num = list(map(int, str_num))
	sum_num = sum(list_num)
	num = sum_num * 10 + N[1]
	if num == N:
		break
	cnt += 1
print(cnt)
