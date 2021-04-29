import sys
input = sys.stdin.readline
n = int(input())
member_list = []
for i in range(n):
    age, name = input().rstrip().split()
    age = int(age)
    member_list.append([age, name])
member_list.sort(key=lambda x: x[0])
for i in member_list:
    print(i[0], i[1])