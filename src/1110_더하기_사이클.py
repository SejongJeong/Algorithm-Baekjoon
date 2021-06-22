N = int(input())
num = N
cnt = 0
while True:
	str_num = str(num)
	list_num = list(map(int, str_num))
	sum_num = sum(list_num) % 10
	num = list_num[len(list_num) - 1] * 10 + sum_num
	cnt += 1
	if num == N:
		break
print(cnt)