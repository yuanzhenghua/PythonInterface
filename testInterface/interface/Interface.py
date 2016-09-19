#coding=gbk
import os, time
import glob
import json
from tools.WriteFile import *
from tools.Post import *
from tools.MakeParams import *
from tools.Compare import *
from testInterface.public.CreateHeader import *

class Interface(object):
    
    def interface(self, url, cookie, param, pic, times, result):
        detailData = {}
        detailData["Id"] = 1
        starttime = 0 
        endtime = 0 
        try:
            #params由param+pic
            params = MakeParams().makeParams(param, pic, times)
            starttime = time.time()
            #rs = module.post(url, param) #调用post方法
            rs = Post().post(url, params, CreateHeader().getHeader(), cookie, "multipart/form-data") #传参url, param, Content-Type方法
            endtime = time.time()
            if Compare().compare(result, rs): 
                detailData["result"] = "true"
                detailData["errormessage"] = ""
            else:
                detailData["result"] = "false"
                detailData["errormessage"] = rs
        except Exception as e:
            detailData["result"] = "false"
            detailData["errormessage"] = e
            print "e=",e
        finally:
            detailData["starttime"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(starttime))
            detailData["endtime"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(endtime))
            detailData["executiontime"] = endtime-starttime
            return detailData