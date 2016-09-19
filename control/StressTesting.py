#coding=gbk
import sys, os, time, random
import glob
import json
import importlib
import threading, threadpool, Queue
from tools.WriteFile import *
from tools.ReadFile import *
from testInterface.user.CtedsUserLogin import *
import userBehavior

cast = {"Login", "Login2"} #执行用例编号
caseProbability = {80, 20} #用例执行概率
test_start_time = "2016-07-19 16:52:00" #测试开始时间
test_end_time = "2016-07-19 16:52:05" #测试结束时间
#work_num = 1 #执行总次数
thread_num = 2 #并发次数

#记录数据初始化
global total, success, fail, totalExecutionTime, maxTime, minTime, list_data
total = 0  #总次数
success = 0  #成功次数
fail = 0  #失败次数
totalExecutionTime = 0  #总消耗时间
maxTime = 0 #最大消耗时间
minTime = 10000 #最小消耗时间
list_data = [] #明细记录保存

def do_job(k):
    global total, success, fail, totalExecutionTime, maxTime, minTime, list_data
    total = total+1 #计数器    
    #读取测试数据
    module = importlib.import_module('userBehavior.'+k)
    detailData = module.do().do_work()
    detailData["Id"] = total
    if detailData["result"] == "success":
        success = success+1
    else:
        fail = fail+1
    totalExecutionTime = totalExecutionTime+detailData["executiontime"]
    if maxTime<detailData["executiontime"]:
        maxTime = detailData["executiontime"]
    elif minTime>detailData["executiontime"]:
        minTime = detailData["executiontime"]
    list_data.append(detailData)

def random_pick_odd(some_list, odds):    
    table = [z for x,y in zip(some_list,odds) for z in [x] * y]     
    return random.choice(table)

def save_data(data):
    for d in data:
        WriteFile.WriteXls(FolderPath, d)

if __name__ == '__main__':
    #global total, success, fail, totalExecutionTime, maxTime, minTime, list_data
    FolderPath = WriteFile().Createfolder()
    try:
        pool = threadpool.ThreadPool(thread_num)   
        while True:
            now_time = time.time()
            print "waiting..."
            if ((now_time>=int(time.mktime(time.strptime(test_start_time,'%Y-%m-%d %H:%M:%S'))) and now_time<=int(time.mktime(time.strptime(test_end_time,'%Y-%m-%d %H:%M:%S'))))):
                k = random_pick_odd(cast, caseProbability)
                print k
                requests = threadpool.makeRequests(do_job, {k}) #makeRequests(callable, args_list,callback=None,exc_callback=None)
                [pool.putRequest(req) for req in requests]
                pool.wait()
                if len(list_data)>=100: #每100条记录保存1次
                    l = list_data
                    list_data = []
                    for d in l:
                        WriteFile().WriteXls(FolderPath, d)
            elif (now_time>int(time.mktime(time.strptime(test_end_time,'%Y-%m-%d %H:%M:%S')))):
                break
    except Exception as e:
        print str(e)
    finally:
        if len(list_data)>0:
            for d in list_data:
                WriteFile().WriteXls(FolderPath, d)
        WriteFile().WriteTxt(FolderPath, total, success, fail, totalExecutionTime, maxTime, minTime)
    