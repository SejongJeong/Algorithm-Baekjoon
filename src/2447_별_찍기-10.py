import sys
num = int(input())
def recur_start(i, j):
	while(i != 0):
		if (i % 3 == 1 and j % 3 == 1):
			sys.stdout.write(' ')
			return
		i = i // 3
		j = j // 3
	sys.stdout.write('*')

for i in range(num):
	for j in range(num):
		recur_start(i, j)
	sys.stdout.write('\n')

