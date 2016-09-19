#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class CtedsTopicAdd_t_post(object):
    
    url = "http://open.aliwap.cn:8000/cteds/topic/add_t_post"

    # 回帖，正常获取
    def test_1(self):
        param = {"tid":"241","uid":"4412","content":"hdjsajkkdjalksakd"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 回帖，回帖内容为空
    def test_2(self):
        param = {"tid":"237","uid":"4412","content":""}
        pic = ""
        times = ""
        result = {"status":"1004","message":"内容长度错误"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 回帖，回帖内容小于10个字
    def test_3(self):
        param = {"tid":"237","uid":"4412","content":"aaaaa"}
        pic = ""
        times = ""
        result = {"status":"1004","message":"内容长度错误"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 回帖，帖子删除状态
    def test_4(self):
        param = {"tid":"242","uid":"4412","content":"hdjsajkkdjalksakd"}
        pic = ""
        times = ""
        result = {"status":"1004","message":"回复的帖子已删除或不存在"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 回帖，回帖内容大于700个字
    def test_5(self):
        content = ""
        for i in range(150):
            content = content + "测试超过700字"
        param = {"tid":"242","uid":"4412","content":"hdjsajkkdjalksakd"}
        param["content"] = content
        pic = ""
        times = ""
        result = {"status":"1004","message":"内容长度错误"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    