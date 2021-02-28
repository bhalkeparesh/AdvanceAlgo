# sortest job first
# non-preamtive algorithm
import heapq
ready =[{'id':1,'at':3,'bt':4},
		{'id':2,'at':0,'bt':5},
		{'id':3,'at':3,'bt':10},
		{'id':4,'at':4,'bt':4},
		{'id':4,'at':1,'bt':4}
]

def sjf(ready):
	ready_queue =[]
	terminated =[]
	for process in ready:
		ready_queue.append(process)
	curr_time=0
	ready_queue.sort(key=lambda x:x['bt'])
	while(ready_queue):
		for process in ready_queue:
			if(process['at']<=curr_time):
				print(f"Executing the process: {process['id']}")
				process['ct']=curr_time
				process['wt']=curr_time-process['at']
				curr_time+=process['bt']
				terminated.append(process)
				ready_queue.remove(process)


	print(*terminated,sep="\n")

sjf(ready)