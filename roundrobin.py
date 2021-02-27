#round robin algorithm
#Process_id arrival_time burst_time 
from collections import deque

ready =[{'id':1,'at':3,'bt':4},
		{'id':2,'at':0,'bt':5},
		{'id':3,'at':3,'bt':10},
		{'id':4,'at':4,'bt':4},
		{'id':4,'at':1,'bt':4}
]
#round round function
def round_robin(ready):
	quantum_time=2
	terminated =[]
	ready_queue=deque()
	for process in sorted(ready,key=lambda x: x['at']):
		ready_queue.append(process)
	total_time=0
	while(ready_queue):
		curr_process = ready_queue.popleft()
		if(curr_process["bt"]>0):
			print(f"Executing Process {curr_process['id']}...")
			if(curr_process["bt"]>2):
				curr_process["bt"]-=2
				total_time+=2
				ready_queue.append(curr_process)
			else:
				total_time+=curr_process["bt"]
				curr_process['ct']=total_time
				curr_process['wt']=total_time-curr_process['at']
				terminated.append(curr_process)
				curr_process["bt"]=0

	print(terminated)
#terminated stores all datails of process after termination



#function call
round_robin(ready)