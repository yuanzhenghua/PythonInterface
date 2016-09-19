#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class CtedsUserLogin(object):    
    url = "http://open.aliwap.cn:8000/cteds/user/login"

    # 登录，账号和密码都正确
    def test_1(self):
        param = {"username":"18067951267","password":"123456"}
        pic = ""
        times = ""
        result = {"status": 10000}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData

    # 登录，账号不存在
    def test_2(self):
        param = {"username":"1806795126","password":"123456"}
        pic = ""
        times = ""
        result = {"message": "帐号或密码不正确", "name": "username_error"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 登录，密码错误
    def test_3(self):
        param = {"username":"18067951267","password":"12345"}
        pic = ""
        times = ""
        result = {"message": "帐号密码不正确", "name": "password_error"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 登录，密码为空
    def test_4(self):
        param = {"username":"18067951267","password":""}
        pic = ""
        times = ""
        result = {"message": "帐号密码不正确", "name": "password_error"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 登录，账号为空
    def test_5(self):
        param = {"username":"","password":"123456"}
        pic = ""
        times = ""
        result = {"message": "帐号密码不正确", "name": "password_error"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData