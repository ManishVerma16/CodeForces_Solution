def petyaString(arr1, arr2):
	flag = 0
	for i in range(len(arr1)):
		if ord(arr1[i]) < ord(arr2[i]):
			flag = -1
			break
		elif ord(arr1[i]) > ord(arr2[i]):
			flag = 1
			break
		else:
			continue
	if flag == -1:
		print(-1)
	elif flag == 1:
		print(1)
	else:
		print(0)

arr1 = list(input().lower())
arr2 = list(input().lower())
petyaString(arr1, arr2)
