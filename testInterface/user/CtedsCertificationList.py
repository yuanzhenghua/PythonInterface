#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class CtedsCertificationList(object):
    
    url = "http://open.aliwap.cn:8000/cteds/certification/list"
    siteid = "1"

    # 实名申请列表，正常情况
    def test_1(self):
        param = {"siteid":""}
        param["siteid"] = self.siteid
        pic = {}
        times = {}
        result = {"status": 10000}
        detailedData = CtedsCertificationList().Implementation(param, pic, times, result)
        return detailedData
    