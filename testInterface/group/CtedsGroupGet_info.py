#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class CtedsGroupGet_info(object):
    
    url = "http://open.aliwap.cn:8000/cteds/group/get_info"

    # 圈子信息，正常获取
    def test_1(self):
        param = {"gid":"55","uid":"4412"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 圈子信息，没有uid信息
    def test_2(self):
        param = {"gid":"55","uid":""}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 圈子信息，uid不存在
    def test_3(self):
        param = {"gid":"55","uid":""}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 圈子信息，没有gid信息
    def test_4(self):
        param = {"gid":"","uid":"4412"}
        pic = ""
        times = ""
        result = {"status": "1004", "message": "参数错误"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 圈子信息，gid不存在
    def test_5(self):
        param = {"gid":"123456","uid":"4412"}
        pic = ""
        times = ""
        result = {"status": "1004", "message": "参数错误"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    