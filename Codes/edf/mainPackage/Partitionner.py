from mainPackage.Processor import Processor
from mainPackage.Task import Task
import csv


class Partitioner:
    

    # considering that each processor's utilization is equal to 1
    # tasks might be sorted in an increasing or decreasing order
    def __init__(self, task_file_name):  # Receiving the file name containing the task set as a parameter
        
        self.__task_file_name = task_file_name
        self.__tasks__ = []
        self.__processors__ = []

    def bestFit(self):
        
        self.__bestWorstFit(True)

    def worstFit(self):
        

        self.__bestWorstFit(False)

    def nextFit(self):
        
        self.__processors__ = []  # Making sure that the processor array is empty
        current_p = Processor()  # If it doesn't fit then a new bin (processor) is created
        # current_p refers to the the current processor that is considered
        for task in self.__tasks__:
            if task.getUtilization() >= 1:  # not taking into consideration the tasks higher than 1
                continue
            if current_p.addTask(task) == 0:
                self.__processors__.append(current_p)  # appending the previous processor to the list
                current_p = Processor()  # adding a new processor
                current_p.addTask(task)
        self.__processors__.append(current_p)  # appending the last used processor

    def firstFit(self):
        
        self.__processors__ = []  # Making sure that the processor array is empty
        current_p = Processor()
        # pushing the first processor into the processors list
        self.__processors__.append(current_p)
        added = False  # used to keep track of the current index
        for task in self.__tasks__:
            if task.getUtilization() >= 1:  # not taking into consideration the tasks higher than 1
                continue
            for processor in self.__processors__:
                if processor.addTask(task) == 1:
                    added = True
                    break
            if not added:  # in the case where the task was not added to any processor then a new one should be  created
                current_p = Processor()
                current_p.addTask(task)
                self.__processors__.append(current_p)
            added = False

    def sort(self, order):
        
        if order == "ASC":  # Sorting tasks in an ascending utilization
            self.__tasks__ = sorted(self.__tasks__, key=Task.getUtilization)
            return
        else:  # Sorting the tasks in a descending utilization
            self.__tasks__ = sorted(self.__tasks__, reverse=True, key=Task.getUtilization)
            return

    def extractTasks(self):  # it will read the file then extract the task and store them in a list
        
        with open(self.__task_file_name) as tasks_file_name:
            reader = csv.DictReader(tasks_file_name)
            for row in reader:
                task = Task(offset=float(row['offset']),  # It should be converted into float since
                            deadline=float(row["deadline"]),
                            period=float(row["period"]),
                            wcet=float(row["wcet"]),
                            utilization=float(row["utilization"]),
                            number=float(row['number']))
                # appending the tasks to the class attribute
                self.__tasks__.append(task)

    def displayProcessors(self):
        
        for processor in self.__processors__:
            print("[")
            for task in processor.getTasks():
                print(task.toJson())
            print("]" + "\n")

    def getProcessors(self):
        
        return self.__processors__

    def __bestWorstFit(self, reverse: bool):
        

        current_p = Processor()
        processors = [current_p]
        added = False
        for task in self.__tasks__:
            if task.getUtilization() >= 1:  # not taking into consideration the tasks higher than 1
                continue
            # In order to put the task in the best or worst fit processor, processors' load should constantly be ordered
            processors = sorted(processors, reverse=reverse, key=Processor.getCapacity)
            for processor in processors:
                if processor.addTask(task) == 1:
                    added = True
                    break
            if not added:  # in the case where the task was not added to any processor then a new one should be  created
                current_p = Processor()
                current_p.addTask(task)
                processors.append(current_p)
            added = False
        self.__processors__ = processors
