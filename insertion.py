def getData():
	a=list(map(int,input().split()))
	return a

def insertion(arr):
	for i in range(len(arr)):
		key = arr[i]
		j=i-1
		while(j>=0 and key < arr[j]):
			arr[j+1]=arr[j]
			j-=1
		arr[j+1]=key

array = getData()
insertion(array)
print(array)
