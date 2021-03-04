#We can use also list to implement min priority queue
#but complexity will be 
# for  insertion : O(n)
# for deletion : 0(n)
# for getmin : 0(1) since we can store min element

# when we use heap(heapq):
# we can do all operation in O(logn) time complexity

# Import the heap functions from python library 
from heapq import heappush, heappop, heapify 

# heappop - pop and return the smallest element from heap 
# heappush - push the value item onto the heap, maintaining 
#			 heap invarient 
# heapify - transform list into heap, in place, in linear time 

class MinHeap: 
	
	# Constructor to initialize a heap 
	def __init__(self): 
		self.heap = [] 
	#gives the index of parent element
	def parent(self, i): 
		return (i-1)//2
	
	# Inserts a new val in heap 
	def insertKey(self, val): 
		heappush(self.heap, val)		 

	# Decrease value of key at index 'i' to new_val 
	# It is assumed that new_val is smaller than heap[i] 
	def decreaseKey(self, i, new_val): 
		self.heap[i] = new_val 
		while(i != 0 and self.heap[self.parent(i)] > self.heap[i]): 
			# Swap heap[i] with heap[parent(i)] 
			self.heap[i] , self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i] 
			
	# Method to remove minium element from min heap 
	def extractMin(self): 
		return heappop(self.heap) 	

	# This functon deletes key at index i. It first reduces 
	# value to minus infinite and then calls extractMin() 
	def deleteKey(self, i): 
		self.decreaseKey(i, float('-inf')) 
		self.extractMin() 

	# Get the minimum element from the heap 
	def getMin(self): 
		return self.heap[0] 

#testing functions
q = MinHeap() 
q.insertKey(3) 
q.insertKey(2) 
q.deleteKey(1) 
q.insertKey(15) 
q.insertKey(5) 
q.insertKey(4) 
q.insertKey(45) 

#printing the results
print(q.extractMin()) 
print(q.getMin())
q.decreaseKey(2, 1) 
print(q.getMin()) 

