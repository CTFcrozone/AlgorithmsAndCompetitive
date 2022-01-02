n = int(input())

ans = n - 4
ans2 = n - 9 

if n % 2 == 0:
	print("4 " + str(ans))
else:
	print("9 " + str(ans2))