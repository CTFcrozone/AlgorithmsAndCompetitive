tests = int(input())

for test in range(tests):
	a, b, n = map(int, input().split())

	if a > b:
		a, b = b, a

	operation = 0

	while a <= n and b <= n:
		a += b
		a, b = b, a
		operation += 1

	print(operation)

