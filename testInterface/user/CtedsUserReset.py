#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *


class CtedsUserReset(object):
    
    url = "http://open.aliwap.cn:8000/cteds/user/reset"

    # 重置密码，正常情况
    def test_1(self):
        param = {"phone":"18067951267","password":"123456"}
        pic = ""
        times = ""
        result = {"status": 10000, "data": {"is_lost": 0, "ret": 0}}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 重置密码，密码为空
    def test_2(self):
        param = {"phone":"18067951267","password":""}
        pic = ""
        times = ""
        result = {"status": 10000, "data": {"msg": "参数不正确", "is_lost": 0, "ret": 1}}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 重置密码，手机号码错误
    def test_3(self):
        param = {"phone":"4412","password":"123456"}
        pic = ""
        times = ""
        result = {"status": 10000, "data": {"msg": "未注册用手机号", "is_lost": 0, "ret": 1}}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    