import sys
input = sys.stdin.readline
n = int(input())
cnt = 0
final = 0
i = 666
while cnt != n:
    str_i = str(i)
    for each in range(len(str_i)-2):
        if str_i[each:each+3] == '666':
            cnt += 1
            break
    final = i
    i += 1
print(final)


