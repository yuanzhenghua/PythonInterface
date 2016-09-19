#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class CtedsUserCheckMobile(object):
    
    url = "http://open.aliwap.cn:8000/cteds/user/check/mobile"

    # 手机号校验，未注册手机号
    def test_1(self):
        param = {"phone":"13486119817"}
        pic = ""
        times = ""
        result =  {"status": 10000, "data": {"msg": "", "recode": "1", "is_lost": "0", "ret": "0"}}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 手机号校验，已注册手机号
    def test_2(self):
        param = {"phone":"11111111111"}
        pic = ""
        times = ""
        result = {"status": "1004", "message": "不是手机号码"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 手机号校验，手机号中带非数字
    def test_3(self):
        param = {"phone":"1111A111111"}
        pic = ""
        times = ""
        result = {"status": "1004", "message": "不是手机号码"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 手机号校验，手机号中带非数字
    def test_4(self):
        param = {"phone":"1111啊111111"}
        pic = ""
        times = ""
        result = {"status": "1004", "message": "不是手机号码"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 手机号校验，手机号为空
    def test_5(self):
        param = {"phone":""}
        pic = ""
        times = ""
        result = {"status": "1004", "message": "参数错误"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    