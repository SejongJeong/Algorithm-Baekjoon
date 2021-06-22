arr = [0 for _ in range(1000001)]
arr[1] = 1
arr[2] = 2
for i in range(3, 1000001):
	arr[i] = (arr[i-1] + arr[i-2]) % 15746
n = int(input())
print(arr[n])