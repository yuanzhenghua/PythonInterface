#coding=gbk
class CreateHeader(object):
    header = {}
    
    def getHeader(self, cookie):
        self.header['sig']="123456"
        self.header['appId']="10003"
        self.header['accesstoken']="4f85225b04feeb9610626017b830384525f2b562"
        return self.header
    
        