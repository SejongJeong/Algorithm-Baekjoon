import sys
input = sys.stdin.readline
count_list = [0] * 10001
n = int(input().rstrip())
for i in range(n):
    temp = int(input())
    count_list[temp] += 1
for i in range(10001):
    for _ in range(count_list[i]):
        sys.stdout.write(str(i) + "\n")

