#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class CtedsTopicT_list(object):
    
    url = "http://open.aliwap.cn:8000/cteds/topic/t_list"

    # 帖子列表，正常获取
    def test_1(self):
        param = {"gid":"55","page":"1","num":"5","digest":"0"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 帖子列表，省略可选参数
    def test_2(self):
        param = {"gid":"55","page":"","num":"","digest":""}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 帖子列表，列表长度不够
    def test_3(self):
        param = {"gid":"55","page":"2","num":"5","digest":"1"}
        pic = ""
        times = ""
        result = {"status":10000,"data":{"page_total":0,"items":[]}}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 帖子列表，列表长度不够
    def test_4(self):
        param = {"gid":"123456","page":"1","num":"5","digest":"0"}
        pic = ""
        times = ""
        result = {"status":10000,"data":{"page_total":0,"items":[]}}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    