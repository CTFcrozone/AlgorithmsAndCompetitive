k, n, w = map(int, input().split())
costs = 0
for i in range(1, w+1):
	costs = costs + i * k

borrowed = costs - n 
if borrowed < 0:
	borrowed = 0

print(borrowed)