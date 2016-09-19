
class TotalData(object):

    def __init__(self, total, success, fail, totalExecutionTime, maxTime, minTime):
        self.total = total
        self.success = success
        self.fail = fail
        self.totalExecutionTime = totalExecutionTime
        self.maxTime = maxTime
        self.minTime = minTime
    
    def set_total(self, total):
        self.total = total
        
    def get_total(self):
        return self.total
    
    def set_success(self, success):
        self.success = success
        
    def get_success(self):
        return self.success
    
    def set_fail(self, fail):
        self.fail = fail
        
    def get_fails(self):
        return self.fail
    
    def set_totalExecutionTime(self, totalExecutionTime):
        self.totalExecutionTime = totalExecutionTime
        
    def get_totalExecutionTime(self):
        return self.totalExecutionTime
    
    def set_maxTime(self, maxTime):
        self.maxTime = maxTime
        
    def get_maxTime(self):
        return self.maxTime
    
    def set_minTime(self, minTime):
        self.minTime = minTime
        
    def get_minTime(self):
        return self.minTime