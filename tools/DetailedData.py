
class DetailedData(object):

    def __init__(self, no, name, fileName, startTime, endTime, executionTime, result, errorMessage):
        self.no = no
        self.name = name
        self.fileName = fileName
        self.startTime = startTime
        self.endTime = endTime
        self.executionTime = executionTime
        self.result = result
        self.errorMessage = errorMessage
        