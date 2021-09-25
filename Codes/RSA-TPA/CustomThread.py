from SharedObject import *
from threading import Thread

class CustomThread(Thread):
    def __init__(self, shared_object, thread_id, lock, status):
        Thread.__init__(self)
        self.shared_object = shared_object
        self.thread_id = thread_id
        self.lock = lock
        self.status = status
        self.setStop(True)
        self.start()

    def setTask(self,task_id):
        self.task_id = task_id

    def getTask(self):
        return self.task_id

    def setStop(self,runThread):
        self.runThread = runThread

    def getStop(self):
        return self.runThread
    
    def run(self):
        while self.getStop():
            if self.status == 1:
                self.shared_object.executeTask(self.thread_id,self.lock,self.getTask())
                self.status = 0
