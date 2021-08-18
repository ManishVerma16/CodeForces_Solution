def dislikeThree(num):
	i, c = 1, 1
	while i<num:
		c += 1
		if c % 3 == 0 or '3' in str(c)[-1]:
			continue
		else:
			i += 1

	print(c)

	


t = int(input())
while t>0:
	t -= 1
	n = int(input())
	dislikeThree(n)
