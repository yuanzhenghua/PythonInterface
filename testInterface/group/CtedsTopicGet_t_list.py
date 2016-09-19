#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class CtedsTopicGet_t_list(object):
    
    url = "http://open.aliwap.cn:8000/cteds/topic/get_t_info"

    # 贴子信息，正常获取
    def test_1(self):
        param = {"tid":"233"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 贴子信息，帖子id为空
    def test_2(self):
        param = {"tid":""}
        pic = ""
        times = ""
        result = {"status":"1004","msg":"参数错误"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 贴子信息，帖子已被删除
    def test_3(self):
        param = {"tid":"234"}
        pic = ""
        times = ""
        result = {"status":"1004","msg":"帖子已删除"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 贴子信息，帖子不存在
    def test_4(self):
        param = {"tid":"123456"}
        pic = ""
        times = ""
        result = {"status":"1004","msg":"帖子不存在"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    