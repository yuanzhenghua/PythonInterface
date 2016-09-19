#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class CtedsGroupQuit_group(object):
    
    url = "http://open.aliwap.cn:8000/cteds/group/quit_group"

    # 退出圈子，正常退出
    def test_1(self):
        param = {"gid":"55","uid":"4412"}
        pic = ""
        times = ""
        result = {"status": 10000, "data": {"is_lost": 0, "ret": 0}}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 退出圈子，加入已加入圈子
    def test_2(self):
        param = {"gid":"55","uid":"4412"}
        pic = ""
        times = ""
        result = {"status":"1004","msg":"您不在圈子内"}
        CtedsGroupQuit_group().Implementation(param, pic, times, result)
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 退出圈子，已关闭圈子
    def test_3(self):
        param = {"gid":"2","uid":"4412"}
        pic = ""
        times = ""
        result = {"status":"1004","msg":"圈子已关闭"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 退出圈子，圈子不存在
    def test_4(self):
        param = {"gid":"123456","uid":"4412"}
        pic = ""
        times = ""
        result = {"status": "1003", "message": "圈子不存在"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 退出圈子，圈子id为空
    def test_5(self):
        param = {"gid":"","uid":"4412"}
        pic = ""
        times = ""
        result = {"status": "1004", "message": "参数错误"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 退出圈子，用户id为空
    def test_6(self):
        param = {"gid":"55","uid":""}
        pic = ""
        times = ""
        result = {"status": "1004", "message": "参数错误"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 退出圈子，用户id为账号
    def test_7(self):
        param = {"gid":"55","uid":"18067951267"}
        pic = ""
        times = ""
        result = {"status": 10003, "message": "参数错误或用户不存在。"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
