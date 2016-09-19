#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class NewsDelete(object):
    
    url = "http://open.aliwap.cn:8000/news/delete"

    # 删除新闻，正常情况
    def test_1(self):
        param = {"id":"27"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 删除新闻，已删除
    def test_2(self):
        param = {"id":"27"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 删除新闻，id不存在
    def test_3(self):
        param = {"id":"10000"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 删除新闻，id为空
    def test_4(self):
        param = {"id":""}
        pic = ""
        times = ""
        result = {"status": "1004", "message": "参数错误"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
