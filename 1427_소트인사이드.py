import sys
input = sys.stdin.readline
num = input().rstrip()
num_list = list(map(int, num))
num_list.sort(reverse=True)
print(''.join(map(str,num_list)))