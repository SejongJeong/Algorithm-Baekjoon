import sys
input = sys.stdin.readline
N = int(input())
cnt = 0
for _ in range(N):
	check = [False for _ in range(26)]
	com = False
	word = input().rstrip()
	prev = ''
	for i, w in enumerate(word):
		if prev != w:
			if check[ord(w)-97]:
				com = True
				break
		check[ord(w)-97] = True
		prev = w
	if not com:
		cnt += 1
print(cnt)


# result = 0
# for i in range(int(input())):
#     word = input()
#     if list(word) == sorted(word, key=word.index):
#         result += 1
# print(result)