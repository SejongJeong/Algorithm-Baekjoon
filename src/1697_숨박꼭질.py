from collections import deque
n, k = map(int, input().split())
l = [False for _ in range(100001)]
q = deque()
q.append(n)
l[n] = True
cnt = 0
chk = False
while q:
	len_q = len(q)
	for _ in range(len_q):
		x = q.popleft()
		if x == k:
			chk = True
			break
		if 0<=(2*x)<100001 and not l[2*x]:
			q.append(2*x)
			l[2*x] = True
		if 0<=(x-1)<100001 and not l[x-1]:
			q.append(x-1)
			l[x-1] = True
		if 0<=(x+1)<100001 and not l[x+1]:
			q.append(x+1)
			l[x+1] = True
	if chk:
		break
	cnt += 1
print(cnt)


# Recursion (faster than my code)
# def c(n,k):
#     if n>=k:
#         return n-k
#     elif k == 1:
#         return 1
#     elif k%2:
#         return 1+min(c(n,k-1),c(n,k+1))
#     else:
#         return min(k-n, 1+c(n,k//2))
    
# n, k = map(int,input().split())
# print(c(n,k))