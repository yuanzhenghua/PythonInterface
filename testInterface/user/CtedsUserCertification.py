#coding=gbk
from tools.MySQL import *
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *
from testInterface.user.CtedsUserLogin import *

class CtedsUserCertification(object):
    
    url = "http://open.aliwap.cn:8000/cteds/user/certification"
    siteid = "1"

    # 实名认证，未提交过账号
    def test_1(self):
        param = {"truename":"aaa","idcard":"330106198706022014","uid":"","siteid":""}
        param["siteid"] = self.siteid
        param["uid"], self.header["token"] = self.init()
        pic = {"faceImg":"F:\\aaa.jpg","backImg":"F:\\aaa.jpg"}
        times = ""
        result = {"status": 10000, "data": {"correct": {"message": "实名认证提交成功！", "code": "200"}}}
        MySQL().ExecNonQuery("edusohodb", "UPDATE user SET approvalStatus = 'unapprove' WHERE id ="+ param["uid"])
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 实名认证，审核中账号
    def test_2(self):
        param = {"truename":"bbb","idcard":"330106198706022014","uid":"","siteid":""}
        param["siteid"] = self.siteid
        param["uid"], self.header["token"] = self.init()
        self.init()
        pic = {"faceImg":"F:\\aaa.jpg","backImg":"F:\\aaa.jpg"}
        times = ""
        result = {"status": "10005", "message": "用户已通过实名认证或正在审核"}
        MySQL().ExecNonQuery("edusohodb", "UPDATE user SET approvalStatus = 'approving' WHERE id ="+ param["uid"])
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 实名认证，审核失败账号
    def test_3  (self):
        param = {"truename":"bbb","idcard":"330106198706022014","uid":"","siteid":""}
        param["siteid"] = self.siteid
        param["uid"], self.header["token"] = self.init()
        self.init()
        pic = {"faceImg":"F:\\aaa.jpg","backImg":"F:\\aaa.jpg"}
        times = ""
        result = {"status": 10000, "data": {"correct": {"message": "实名认证提交成功！", "code": "200"}}}
        MySQL().ExecNonQuery("edusohodb", "UPDATE user SET approvalStatus = 'approve_fail' WHERE id ="+ param["uid"])
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 实名认证，审核通过账号
    def test_4  (self):
        param = {"truename":"bbb","idcard":"330106198706022014","uid":"","siteid":""}
        param["siteid"] = self.siteid
        param["uid"], self.header["token"] = self.init()
        self.init()
        pic = {"faceImg":"F:\\aaa.jpg","backImg":"F:\\aaa.jpg"}
        times = ""
        result = rs= {"status": "10005", "message": "用户已通过实名认证或正在审核"}
        MySQL().ExecNonQuery("edusohodb", "UPDATE user SET approvalStatus = 'approved' WHERE id ="+ param["uid"])
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 实名认证，真实姓名为空
    def test_5  (self):
        param = {"truename":"","idcard":"330106198706022014","uid":"","siteid":""}
        param["siteid"] = self.siteid
        param["uid"], self.header["token"] = self.init()
        self.init()
        pic = {"faceImg":"F:\\aaa.jpg","backImg":"F:\\aaa.jpg"}
        times = ""
        result = {"status": "10005", "message": "用户已通过实名认证或正在审核"}
        MySQL().ExecNonQuery("edusohodb", "UPDATE user SET approvalStatus = 'unapprove' WHERE id ="+ param["uid"])
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 实名认证，身份证为空
    def test_6  (self):
        param = {"truename":"bbbb","idcard":"","uid":"","siteid":""}
        param["siteid"] = self.siteid
        param["uid"], self.header["token"] = self.init()
        self.init()
        pic = {"faceImg":"F:\\aaa.jpg","backImg":"F:\\aaa.jpg"}
        times = ""
        result = {"status": "10005", "message": "用户已通过实名认证或正在审核"}
        MySQL().ExecNonQuery("edusohodb", "UPDATE user SET approvalStatus = 'unapprove' WHERE id ="+ param["uid"])
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 实名认证，身份证图片为空
    def test_7  (self):
        param = {"truename":"bbb","idcard":"330106198706022014","uid":"","siteid":""}
        param["siteid"] = self.siteid
        param["uid"], self.header["token"] = self.init()
        self.init()
        pic = {}
        times = ""
        result = {"status": "10006", "message": "身份证扫描件必须上传正反两面"}
        MySQL().ExecNonQuery("edusohodb", "UPDATE user SET approvalStatus = 'unapprove' WHERE id ="+ param["uid"])
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    def init(self):
        param = {"username":"18067951267","password":"123456"}
        pic = ""
        times = ""
        result = Post().post(CtedsUserLogin.url, MakeParams().makeParams(param, pic, times), self.header, "multipart/form-data")
        return result["data"]["user"]["id"], result["data"]["token"]
