from queue import Queue
from random import randint
import threading
import time

class SharedObject:

    def __init__(self, sort_list):
         self.sort_list = sort_list

    def accessObject(self,thread_id,task_id):
        start_time = time.time()
        print('Thread '+str(thread_id)+' starts accessing shared object for task '+str(task_id)+" at time : "+str(start_time))
        q = []
        for i in range(0,5):
            value = randint(10, 100)
            q.append(value)
        end_time = time.time()
        value = self.sort_list.get(thread_id) + (end_time - start_time)
        self.sort_list[thread_id] = value
        print('Thread '+str(thread_id)+' task completed and releasing shared Object : '+str(q)+' for task '+str(task_id)+" Finished at time "+str(end_time)+" Execution Time "+str(value))

    def executeTask(self,thread_id,lock,task_id):
        lock.acquire() 
        self.accessObject(thread_id,task_id) 
        lock.release() 
        
