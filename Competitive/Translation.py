def translation(word, wordr):
	if word[::-1] != wordr:
		return "NO"
	else:
		return "YES"

a = str(input())
b = str(input())
print(translation(a, b))