arr = [2, 3, 10, 6, 4, 8, 1]

smallest = arr[0]
diff = arr[1]-arr[0]

for i in range(1,len(arr)):
	if arr[i]-smallest > diff:
		diff = arr[i]-smallest
	if arr[i]<smallest:
		smallest = arr[i]
print(diff)
