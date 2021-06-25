n = int(input())

# Dynamic Programming

# fibo = [0 for _ in range(21)]
# fibo[1] = 1
# for i in range(2, n+1):
# 	fibo[i] = fibo[i-2] + fibo[i-1]
# print(fibo[n])

# Recursion

def fibo(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibo(n-2) + fibo(n-1)
print(fibo(n))

