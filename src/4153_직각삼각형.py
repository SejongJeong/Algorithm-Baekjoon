import sys
input = sys.stdin.readline
while True:
	a, b, c = map(int, input().rstrip().split())
	if a == 0 and b == 0 and c == 0:
		break
	leg = [a, b, c]
	hypotenuse = max(leg)
	leg.remove(hypotenuse)
	if leg[0]**2 + leg[1]**2 == hypotenuse**2:
		print("right")
	else:
		print("wrong")