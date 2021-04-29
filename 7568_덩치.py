import sys
input = sys.stdin.readline
num = int(input())
human_list = [list(map(int,input().split())) for _ in range(num)]
rank = [1 for _ in range(num)]
for i in range(num):
    for j in range(num):
        if human_list[i][0] < human_list[j][0] and human_list[i][1] < human_list[j][1]:
            rank[i] += 1
print(*rank)
