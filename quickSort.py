def getData():
	a=list(map(int,input().split()))
	return a

def quick_sort(array):
	quick_sort2(array,0,len(array)-1)

def findPivot(arr,low,high):
	mid =(low + high)//2
	pivot = high
	if(arr[low]<arr[mid]):
		if(arr[mid] < arr[high]):
			pivot = mid
	else:
		if(arr[low] < arr[high]):
			pivot = low
	return pivot

def quick_sort2(arr,low,high):
	if(low<high):
		p=partition(arr, low, high)
		quick_sort2(arr, low, p-1)
		quick_sort2(arr, p+1, high)
def partition(arr,low,high):
	pivot = findPivot(arr, low, high)
	pivot_element = arr[pivot]
	#print(pivot_element)
	arr[low],arr[pivot]=arr[pivot],arr[low]
	border = low
	for i in range(low,high+1):
		if(arr[i] < pivot_element ):
			border+=1
			arr[i],arr[border] = arr[border],arr[i]
	arr[border],arr[low]=arr[low],arr[border]
	return border






array = getData()
quick_sort(array)
print(array)