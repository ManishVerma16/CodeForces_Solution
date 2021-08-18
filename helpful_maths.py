def helpfulMaths(arr1):
	arr1.sort()
	newString = '+'.join(arr1)
	print(newString)

arr1 = list(input().split('+'))
helpfulMaths(arr1)
