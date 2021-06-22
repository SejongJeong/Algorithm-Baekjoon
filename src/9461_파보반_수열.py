tri = [1 for _ in range(101)]
tri[3] = 2
tri[4] = 2
for i in range(5, 101):
	tri[i] = tri[i-1] + tri[i-5]
T = int(input())
for _ in range(T):
	n = int(input())
	print(tri[n-1])
