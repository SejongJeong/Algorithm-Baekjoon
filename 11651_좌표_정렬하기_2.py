import sys
input = sys.stdin.readline
numbers = []
n = int(input())
for _ in range(n):
    temp = list(map(int, input().rstrip().split()))
    numbers.append(temp)
numbers.sort(key= lambda x : (x[1], x[0]))
for i in range(n):
    print(numbers[i][0], numbers[i][1])