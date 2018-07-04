import resource
import globalVar
import travian

class task:
    def __init__(self ,taskName, taskType, taskObjID = 0):
        print(globalVar.LOGINFO + '[ADD TASK: ' + str(taskName) + ' TYPE: ' + str(taskType) + ' ID: ' + str(
            taskObjID) + ']')
        self.name = taskName
        self.type = taskType
        if (self.type == globalVar.TASKTYPE[0]):
            self.obj = taskObjID
