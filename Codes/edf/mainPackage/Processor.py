from mainPackage.Task import Task



class Processor:
    def __init__(self):
        self.__tasks__ = []
        self.__capacity__ = 0  # keeping track of the processor capacity

    def getCapacity(self):
        
        return self.__capacity__

    # this function allow adding tasks after verifying the capacity criteria
    def addTask(self, task: Task) -> int:
        
        if self.__capacity__ + task.getUtilization() <= 1:
            self.__tasks__.append(task)
            self.__capacity__ = self.__capacity__ + task.getUtilization()
            return 1
        else:
            return 0

    def getTasks(self):
        return self.__tasks__
