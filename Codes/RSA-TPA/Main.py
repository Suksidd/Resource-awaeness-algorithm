from SharedObject import *
import threading
from random import randint
from CustomThread import *
from random import randint

from Task import *

print("Enter number of task : ")
num_task = int(input())
print("Enter number of cores : ")
num_cores = int(input())

priority_list = {}
for i in range(0,num_task):
    value = randint(1, 10)
    priority_list[i] = value

print("\nPriority for each task")
for key,value in priority_list.items():
    print("Task "+str(key)+" Priority = "+str(value))

priority_list = sorted(priority_list.items(), key=lambda x: x[1])
priority_list = {k: v for k, v in priority_list} 
task_list = []
print("\nSorted Priority Tasks")
for key,value in priority_list.items():
    print("Task "+str(key)+" Priority = "+str(value))
    t = Task()
    t.setTaskname(key)
    t.setPriority(value)
    task_list.append(t)
    

sort_list = {}

lock = threading.Lock()   
so = SharedObject(sort_list) 

thread_list = [] 

for i in range(0,num_cores):
    ct = CustomThread(so,i,lock,0) 
    thread_list.append(ct) 
    sort_list[i] = 0  

i = 0
while i < num_task:  
    t = task_list[i]
    efficient_thread = sorted(sort_list.items(), key=lambda x: x[1]) 
    search_core = {k: v for k, v in efficient_thread} 
    
    j = list(search_core.keys())[0] 
    ct = thread_list[j] 
    
    if ct.status == 0:
        
        ct.setTask(t.getTaskname())
        
        ct.status = 1
        
        i = i + 1
        

for i in range(0,num_cores):
    ct = thread_list[i]
    ct.setStop(False)
    ct.join()
    

print('\nAll Threads Utilization Time\n\n')
utilization_time = []
for i in range(0,num_cores):
     print("Thread "+str(i)+" Utilization Time : "+str(sort_list.get(i)))
     utilization_time.append(sort_list.get(i))


