def luckyNumber(num):
	flag = 0
	count = 0
	for i in num:
		if (4 == int(i)) or (7 == int(i)):
			count += 1


	if count==7 or count==4:
		print('YES')
	else:
		print('NO')

num = input()
luckyNumber(num)