# coding=utf-8
while True:
	a, b = map(int, input().split())
	try:
		result = a / b
		if (result - int(a / b) >= 0.5):
			result += 0.5
		print(int(result))
	except Exception as e:
		print("error")