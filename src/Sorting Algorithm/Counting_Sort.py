import sys
input = sys.stdin.readline
count_list = [0] * 10001
n = int(input().rstrip())
original_list = [0] * n
for i in range(n):
    temp = int(input())
    count_list[temp] += 1
    original_list[i] = temp
for i in range(10000):
    count_list[i+1] += count_list[i]
sorted_list = [0] * n
for i in range(n):
    count_list[original_list[i]] -= 1
    sorted_list[count_list[original_list[i]]] = original_list[i]
print('\n'.join(map(str,sorted_list)))

