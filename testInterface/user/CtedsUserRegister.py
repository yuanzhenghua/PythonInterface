#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *


class CtedsUserRegister(object):
    
    url = "http://open.aliwap.cn:8000/cteds/user/register"
    
    # 注册，新手机号注册
    def test_1(self):
        param = {"phone":"13486119817","type":"1","password":"123456"}
        pic = ""
        times = ""
        result = {"ret":"0"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 注册，已注册手机号注册
    def test_2(self):
        param = {"phone":"13486119817","type":"1","password":"123456"}
        pic = ""
        times = ""
        result = {"ret":"1","msg":"手机号已注册"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 注册，非纯数字手机号注册
    def test_3(self):
        param = {"phone":"1111啊啊11111","type":"1","password":"123456"}
        pic = ""
        times = ""
        result = {"ret":"1","msg":"手机号格式错误"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 注册，密码为空
    def test_4(self):
        param = {"phone":"13486119819","type":"1","password":""}
        pic = ""
        times = ""
        result = {"ret":"1","msg":"手机号已注册"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    