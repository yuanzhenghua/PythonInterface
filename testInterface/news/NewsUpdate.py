#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class NewsUpdate(object):
    
    url = "http://open.aliwap.cn:8000/news/update"

    # 修改新闻，正常情况
    def test_1(self):
        param = {"id":"24", "title":"测试测试12","username":"18067951267","content":"测试测试","keywords":"测试","description":"test"}
        pic = {"thumb":"F:\\aaa.jpg"}
        times = ""
        result = {"status": 10000, "data": 1}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 修改新闻，已删除新闻
    def test_2(self):
        param = {"id":"27", "title":"测试测试13","username":"18067951267","content":"测试测试","keywords":"测试","description":"test"}
        pic = {"thumb":"F:\\aaa.jpg"}
        times = ""
        result = {"status": 10000, "data": 1}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 修改新闻，省略未修改字段
    def test_3(self):
        param = {"id":"29", "title":"测试测试13"}
        pic = {}
        times = ""
        result = {"status": "1004", "message": "参数错误"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    