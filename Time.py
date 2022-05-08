def printString(n):
	
	arr = [0] * 10000
	i = 0

	# Step 1: Converting to number
	# assuming 0 in number system
	while (n > 0):
		arr[i] = n % 26
		n = int(n // 26)
		i += 1
		
	#Step 2: Getting rid of 0, as 0 is
	# not part of number system
	for j in range(0, i - 1):
		if (arr[j] <= 0):
			arr[j] += 26
			arr[j + 1] = arr[j + 1] - 1

	for j in range(i, -1, -1):
		if (arr[j] > 0):
			print(chr(ord('A') +
				(arr[j] - 1)), end = "");

	print();

# Driver code
if __name__ == '__main__':

    # for i in range(28,54):
    #     n = (25 * i) + i
    #     printString(n)
    printString(1378)
# This code is contributed by Princi Singh
