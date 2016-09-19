#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *
from tools.MySQL import *

class CtedsUserInfo(object):
    
    url = "http://open.aliwap.cn:8000/cteds/user/info"

    #获取用户信息，正确情况
    def test_1(self):
        param = {"uid":""}
        param["uid"] = str(MySQL().ExecQuery("eds2015", "SELECT uid FROM member_base WHERE mobile = '18067951267'")[0][0])
        login = Post().post("http://open.aliwap.cn:8000/cteds/user/login", self.header, {"username":"18067951267","password":"123456"}, "multipart/form-data")
        self.header["token"] = login["data"]["token"]
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 获取用户信息，uid为空
    def test_2(self):
        param = {"uid":""}
        login = Post().post("http://open.aliwap.cn:8000/cteds/user/login", self.header, {"username":"18067951267","password":"123456"}, "multipart/form-data")
        self.header["token"] = login["data"]["token"]
        pic = ""
        times = ""
        result = {"status": 10000, "data": {"code": 11000}}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    