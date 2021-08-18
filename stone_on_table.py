def stoneOnTable(arr, n):
	count = 0
	for i in range(1, n):
		if arr[i-1] == arr[i]:
			count += 1
	print(count)

n = int(input())
arr = list(input())
stoneOnTable(arr, n)
