
def getData():
	a=list(map(float,input().split()))
	return a
def insertionSort(arr):
	for i in range(len(arr)):
		key=arr[i]
		j=i-1
		while(j>=0 and key<arr[j]):
			arr[j+1]=arr[j]
			j-=1
		arr[j+1]=key
def bucketSort(arr):
	k,slot=0,10
	#creating buckets depend on given array range
	buckets =[[] for _ in range(slot)]

	#adding value to the buckets
	for i in arr:
		index = int(i*10)
		buckets[index].append(i)
	#sorting bucket
	for bucket in buckets:
		insertionSort(bucket)
	
	# #
	# [arr.extend(b) for b in buckets]
	# return arr[n:]
	for i in range(slot):
		for j in range(len(buckets[i])):
			arr[k]=buckets[i][j]
			k+=1
	return arr



array = getData()
bucketSort(array)
print(array)