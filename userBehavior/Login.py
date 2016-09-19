#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class do(object):

    def do_work(self):
        detailData = self.login()
        return detailData
    
    def login(self):
        url = "http://open.aliwap.cn:8000/cteds/user/login"
        param = {"username":"18067951267","password":"123456"}
        pic = ""
        times = ""
        result = {"status": 10000}
        detailData = Interface().interface(url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData