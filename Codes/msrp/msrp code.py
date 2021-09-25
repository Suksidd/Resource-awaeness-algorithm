import json
import copy
import operator
import random
from sys import *
from math import gcd
import math
import numpy as np
import time


# Data structure to store the task sets

class task:
    def _init_(self, task_id=None, deadline=None, e=None,U=None,s1=None,s2=None,p=None):
        self.task_id = task_id
        self.deadline= deadline
        self.U = U
        self.e = e
        self.s1 = s1     #semaphore 1
        self.s2 = s2
        self.p = p

def read_data():
    global n  # Number of tasks to be partitioned
    global tasks,ts# List that stores the instances of tasks
    tasks = []
    ts=[]
    print("\nEnter no of tasks",  ":")
    n = int(input())
    global prem,prem2,s1t,s2t,s1c,s2c,so,leng,availtasks,uf,t,j,prempt,s3,t
    j=0
    t=0
    prempt=0
    leng=0
    uf=0
    t=0
    prem =[]
    prem2 = []
    s1t=[]
    s2t=[]
    s3=[]
    so=[]
    for i in range(n):
        task_id = i+1
        print("\nEnter phase of task T", i, ":")
        p= int(input())
        print("\nEnter deadline of task T", i, ":")
        deadline = int(input())
        print("Enter the non criticalexcecution time of task C", i, ":")
        e = int(input())
        print("\nEnter semaphore1 of task T", i, ":")
        s1 = int(input())
        print("\nEnter semaphore2 of task T", i, ":")
        s2 = int(input())

        U=(e+s1+s2)/deadline
        uf=uf+U
        leng=leng+e+s1+s2
        tasks.append(task(task_id,deadline,e, U, s1,s2,p))
    ts=tasks
    tasks = sorted(tasks, key=lambda tasks: tasks.deadline)


    for i in range(0,n):
        #prem.append(i)
        #prem[i]=n-i #premption values of sorted list
        so.append(i)
        so[i] =tasks[i].task_id
        if tasks[i].s1!=0:
            s1t.append(i)
            s1t[i]=tasks[i].task_id
        else:
            s1t.append(i)
            s1t[i]=0
        if tasks[i].s2!=0:
            s2t.append(i)
            s2t[i]=tasks[i].task_id
        else:
            s2t.append(i)
            s2t[i]=0
    #
    for i in range(n):
        if s1t[i]!= 0:
            prem.append(i)
            prem[i] = n - so.index(s1t[i])   # to find premption levels of the tasks using semaphore 1
        else:
            prem.append(i)
            prem[i] = 0

    for i in range(n):
        if s2t[i]!=0:
            prem2.append(i)
            prem2[i] = n - so.index(s2t[i]) # to find premption levels of te tasks using semaphore 2
        else:
            prem2.append(i)
            prem2[i] = 0

    s1c = max(prem)
    s2c = max(prem2)
    #for i in 2:
     #   s3[i]=ts[i].task_id
    #for i in range(2):
     #   prempt[i] = 2 - s3.index(tasks[i])  # to find premption levels of the tasks using semaphore 2

start_time = time.time()
def write_data():
        for i in range(n):
            print("-----------------")
            print("TASK  ", tasks[i].task_id)
            print("-----------------")
            print("deadline  ", tasks[i].deadline)
            print("non critical excecution time       ", tasks[i].e)
            print("semaphore1    ", tasks[i].s1)
            print("semaphore2   ", tasks[i].s2)
            print("Utilization", tasks[i].U)
            print("premption level ",so[i])
            print("phase", tasks[i].p)
            print("-----------------")
            print("\n\n")
        print("tasks using resource 1 is")
        for i in range(0,n):
            print("",s1t[i])
        print("tasks using resource 2 is")
        for i in range(0, n):
            print("",s2t[i])

        for i in range(0,n):
            print("premption level of",i+1,"th task is", so[i])
        #for i in range(0, n):
         #   print("prem1", prem[i])
        #for i in range(0, n):
         #   print("prem2", prem2[i]
        print("\n")
        print("celing value of semaphore 1", s1c)
        print("celing value of semaphore 2", s2c)
        print("")

def jum(j,t):

        while(ts[j].e!=0):
                ts[j].e -= 1
                t += 1
                print(" non critical of task ", ts[j].task_id," is running")
                for d in range(0, n):
                    if ts[d].p >= t:
                        ts[d].deadline < ts[j].deadline
                        jum(d, t)

        while(ts[j].s1!= 0):
             ts[j].s1 -= 1
             t += 1
             print(" semaphore 1 of task ", ts[j].task_id, " is running")

             for d in range(j):
                    if ts[d].p >t:
                        if so[d]>=s1c:
                            j=d
                            jum(j,t)

        while ts[j].s2 != 0:
             ts[j].s2 -= 1
             t += 1
             print(" semaphore 2 of task ", ts[j].task_id, " is running")

             for d in range(j):
                    if ts[d].p >t:
                        if so[d]>=s2c:
                            j=d
                            jum(j,t)
read_data()
write_data()
global q
q=5
while q!=0:
    jum(j,t)
    q=q-1

print("--- %s seconds ---" % (time.time() - start_time))