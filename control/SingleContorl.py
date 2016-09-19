#coding=gbk
import os, time
import glob
import json
import importlib
from tools.WriteFile import *
from tools.ReadFile import *
from testInterface.user.CtedsUserCheckMobile import *
from testInterface.user.CtedsUserRegister import *
from testInterface.user.CtedsUserLogin import *
from testInterface.user.CtedsUserInfo import *
from testInterface.user.CtedsUserReset import *
from testInterface.user.CtedsUserCertification import *
from testInterface.user.CtedsUserSendCode import *
from testInterface.user.CtedsCertificationList import *
from testInterface.user.CtedsCertificationVerify import *
from testInterface.user.CtedsCertificationInfo import *
from testInterface.banner.AdBannerGet_banner_list import *
from testInterface.banner.AdBannerPost_banner_list import *
from testInterface.news.NewsLists import *
from testInterface.news.NewsListsCount import *
from testInterface.news.NewsShow import *
from testInterface.news.NewsInsert import *
from testInterface.news.NewsDelete import *
from testInterface.news.NewsUpdate import *
from testInterface.group.CtedsGroupGet_info import *
from testInterface.group.CtedsGroupJoin_group import *
from testInterface.group.CtedsGroupQuit_group import *
from testInterface.group.CtedsTopicT_list import *
from testInterface.group.CtedsTopicGet_t_list import *
from testInterface.group.CtedsTopicT_add import *
from testInterface.group.CtedsTopicGet_t_posts import *
from testInterface.group.CtedsTopicAdd_t_post import *
from testInterface.development.CtedsDevelopmentGet import *

#记录数据初始化
total = 0 #总次数
success = 0 #成功次数,只算执行通过
fail = 0
maxTime = 0  #单次执行最长时间,只算执行通过用例时间
minTime = 99999 #单次执行最端时间,只算执行通过用例时间
totalExecutionTime = 0 #总消耗时间

if __name__ == '__main__':
    #创建测试记录文件夹
    FolderPath = WriteFile().Createfolder()    
    #调用测试类
    detailedData = CtedsTopicT_add().test_7()
    WriteFile().WriteXls(FolderPath, detailedData)
    