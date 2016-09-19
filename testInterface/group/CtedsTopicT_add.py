#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class CtedsTopicT_add(object):
    
    url = "http://open.aliwap.cn:8000/cteds/topic/t_add"

    # 创建帖子，正常创建
    def test_1(self):
        param = {"uid":"4412","name":"接口测试","gid":"55","message":"asdjksakjdjk"}
        pic = {"pic":"F:\\aaa.jpg"}
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 创建帖子，标题少于4个字
    def test_2(self):
        param = {"uid":"4412","name":"11","gid":"55","message":"asdjksakjdjk"}
        pic = {"pic":"F:\\aaa.jpg"}
        times = ""
        result = {"status": 1004, "message": "标题长度不符"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 创建帖子，标题多余25个字
    def test_3(self):
        param = {"uid":"4412","name":"接口测试接口测试接口测试接口测试接口测试接口测试接口测试","gid":"55","message":"asdjksakjdjk"}
        pic = {"pic":"F:\\aaa.jpg"}
        times = ""
        result = {"status": 1004, "message": "标题长度不符"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 创建帖子，内容长度小于10个字
    def test_4(self):
        param = {"uid":"4412","name":"接口测试4","gid":"55","message":"啊啊啊啊啊啊啊"}
        pic = {"pic":"F:\\aaa.jpg"}
        times = ""
        result = {"status": 1004, "message": "内容长度不符"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 创建帖子，内容长度大于700个字
    def test_5(self):
        message = ""
        for i in range(150):
            message = message + "测试超过700字"
        param = {"uid":"4412","name":"接口测试5","gid":"55","message":"asdjksakjdjk"}
        param["message"] = message
        pic = {"pic":"F:\\aaa.jpg"}
        times = ""
        result = {"status": 1004, "message": "内容长度不符"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 创建帖子，图片不传
    def test_6(self):
        param = {"uid":"4412","name":"接口测试6","gid":"55","message":"asdjksakjdjk"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 创建帖子，用户id传错
    def test_7(self):
        param = {"uid":"13486119817","name":"接口测试7","gid":"55","message":"asdjksakjdjk"}
        pic = {"pic":"F:\\aaa.jpg"}
        times = ""
        result = {"status": 1004, "message": "用户未登录或不存在"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 创建帖子，用户传空值
    def test_8(self):
        param = {"uid":"","name":"接口测试8","gid":"55","message":"asdjksakjdjk"}
        pic = {"pic":"F:\\aaa.jpg"}
        times = ""
        result = {"status": 1004, "message": "用户未登录或不存在"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    