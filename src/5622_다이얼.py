word = input()
dic = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0
for cha in word:
	for i, f in enumerate(dic):
		if cha in f:
			time += i + 3
print(time)