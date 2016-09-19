#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class NewsDelete(object):
    
    url = "http://open.aliwap.cn:8000/news/delete"

    # 删除新闻，正常情况
    def test_modile(self):
        cookie = ""
        param = {"id":"27"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, cookie, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
