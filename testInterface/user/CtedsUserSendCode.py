#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class CtedsUserSendCode(object):
    
    url = "http://open.aliwap.cn:8000/cteds/user/sendCode"

    # 实名认证，审核通过账号
    def test_1(self):
        param = {"phone":"13486119817","mcode":"1111"}
        pic = ""
        times = ""
        result = {}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData