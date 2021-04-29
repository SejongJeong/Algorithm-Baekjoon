import sys
input = sys.stdin.readline
n = int(input())
cnt_list = []
for _ in range(n):
    temp  = input().rstrip()
    cnt_list.append((temp, len(temp)))
cnt_list = list(set(cnt_list)) # 이차원일시 Tuple 은 Set으로 변환이 가능 List는 불가
cnt_list.sort(key = lambda x : (x[1], x[0]))
for i in cnt_list:
    print(i[0])
