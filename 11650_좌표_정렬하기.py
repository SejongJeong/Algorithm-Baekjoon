import sys
input = sys.stdin.readline
n =  int(input())
num_list =  []
for _ in range(n):
    temp = list(map(int, input().rstrip().split()))
    num_list.append(temp)
num_list.sort(key = lambda x:(x[0],x[1]))
for i in range(n):
    print(num_list[i][0], num_list[i][1])