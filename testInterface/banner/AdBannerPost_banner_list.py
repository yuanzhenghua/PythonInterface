#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class AdBannerPost_banner_list(object):
    
    url = "http://open.aliwap.cn:8000/ad/banner/post_banner_list"

    # 获取广告    ，正常情况
    def test_1(self):
        param = {"gid":"55","code":"index-banner"}
        pic = ""
        times = ""
        result = {}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 获取广告    ，id为空
    def test_2(self):
        param = {"code":""}
        pic = ""
        times = ""
        result = {"status": "10004", "message": "参数错误【无法匹配】"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData