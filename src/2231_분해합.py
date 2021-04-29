import sys
input = sys.stdin.readline
def di_sum(num):
    result = int(num)
    for each_num in num:
        result += int(each_num)
    return result

num =  int(input())
result = 0
start_num = 0
if num - 9 * len(str(num)) >= 0:
    start_num = num - 9 * len(str(num))
for i in range(start_num, num):
    if di_sum(str(i)) == num:
        result = i
        break
print(result)
