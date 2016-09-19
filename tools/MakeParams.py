#coding=gbk
import json, time

class MakeParams():

    def makeParams(self, param, pic, times):
        params = {} 
        if "" <> param and {} <> param:
            for k in param:
                param[k] = param[k].decode("gbk").encode("utf-8")
            params = dict(params.items()+param.items())
        if "" <> pic and {} <> pic:
            for k in pic:
                pic[k] = open(pic[k].decode("gbk").encode("utf-8"), "rb")
            params = dict(params.items()+pic.items()) 
        if "" <> times and {} <> times: 
            for t in times:
                times[t] = int(time.mktime(time.strptime(times[t],'%Y-%m-%d %H:%M:%S'))) #日期转换成时间戳
            params = dict(params.items()+times.items())
        return params