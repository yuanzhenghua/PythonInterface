#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class NewsLists(object):
    
    url = "http://open.aliwap.cn:8000/news/lists"
    
    # 新闻列表，正常获取
    def test_1(self):
        param = {"start":"1","type":"1","isid":"","offset":"12"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 新闻列表，获取超最大列表范围
    def test_2(self):
        param = {"start":"1000","type":"1","isid":"","offset":"1006"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 新闻列表，省略结束字段值
    def test_3(self):
        param = {"start":"1","type":"1","isid":"","offset":""}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 新闻列表，省略开始字段值
    def test_4(self):
        param = {"start":"","type":"1","isid":"","offset":"6"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 新闻列表，屏蔽新闻
    def test_5(self):
        param = {"start":"1","type":"1","isid":"11","offset":"6"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 新闻列表，类型不存在或取消
    def test_6(self):
        param = {"start":"1","type":"10","isid":"","offset":"6"}
        pic = ""
        times = ""
        result = {"status":"1004","message":"参数错误"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    