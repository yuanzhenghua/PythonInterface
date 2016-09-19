#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class NewsShow(object):
    
    url = "http://open.aliwap.cn:8000/news/show"

    # 新闻详情，正常情况
    def test_1(self):
        param = {"id":"16","type":"1"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 新闻详情，id不存在
    def test_2(self):
        param = {"id":"100","type":"1"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    