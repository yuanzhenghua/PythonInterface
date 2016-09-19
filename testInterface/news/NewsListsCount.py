#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class NewsListsCount(object):
    
    url = "http://open.aliwap.cn:8000/news/listsCount"

    # 新闻列表，正常获取type范围1-4
    def test_1(self):
        param = {"type":"1"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 新闻列表，类型取消或不存在
    def test_2(self):
        param = {"type":"0"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    