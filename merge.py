def getData():
	a=list(map(int,input().split()))
	return a
def merge(arr,low,mid,high):
	a1=arr[low:mid]
	a2=arr[mid:high+1]
	a1.append(9999999999)
	a2.append(9999999999)
	i=j=0
	for k in range(low,high+1):
		if(a1[i] <= a2[j]):
			arr[k]=a1[i]
			i+=1
		else:
			arr[k]=a2[j]
			j+=1


def mergeSort(arr,low,high):
	if(low < high):
		mid = (low+high)//2
		mergeSort(arr, low, mid)
		mergeSort(arr, mid+1, high)
		merge(arr,low,mid,high)

def mergeSort2(array):
	mergeSort(array,0,len(array)-1)
array = getData()


mergeSort2(array)
print(array)