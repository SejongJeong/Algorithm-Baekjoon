N = int(input())
numbers = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())
def solve(plus, minus, multi, div):
	for i in range(4):
		