import sys
import math
from collections import Counter
input = sys.stdin.readline
n = int(input())
num_list = [0 for _ in range(n)]
for i in range(n):
    temp = int(input())
    num_list[i] = temp
print(round(sum(num_list)/n))
num_list.sort()
print(num_list[int(n/2)])
def mode(x):
    count_dic = Counter(x)
    most_count = count_dic.most_common()
    result = None
    if len(x) > 1:
        if most_count[0][1] == most_count[1][1]:
            result = most_count[1][0]
        else:
            result = most_count[0][0]
    else:
        result = most_count[0][0]
    return result
print(mode(num_list))
print(num_list[-1] - num_list[0])
