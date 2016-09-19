#coding=gbk
from testInterface.public.CreateHeader import *
from testInterface.interface.Interface import *

class NewsInsert(object):  
    url = "http://open.aliwap.cn:8000/news/insert"

    # 添加新闻，正常情况
    def test_1(self):
        param = {"title":"测试测试11","username":"18067951267","content":"测试测试","keywords":"测试","description":"test"}
        pic = {"thumb":"F:\\aaa.jpg"}
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 添加新闻，新闻内容文字中带图片
#     def test_2(self):
#         content = "测试  &lt;/p&gt;&lt;p style=&quot;text-align: center;&quot;&gt;&lt;img alt=&quot;\&quot; src=&quot;http://news.edianshang.com/uploadfile/2016/0511/20160511092607215.jpg&quot;/&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;测试"
#         param = {"title":"测试测试12","username":"18067951267","keywords":"测试","description":"test"}
#         param["content"] = content 
#         pic = {"thumb":"F:\\aaa.jpg"}
#         times = ""
#         result = {"status":"10000"}
#         detailedData = NewsInsert().Implementation(param, pic, times, result)
#         return detailedData

    # 添加新闻，标题100个汉字
    def test_3(self):
        title = ""
        for i in range(50):
            title = title + "测试"
        param = {"title":"测试测试11","username":"18067951267","content":"测试测试","keywords":"测试","description":"test"}
        param["title"] = title 
        pic = {"thumb":"F:\\aaa.jpg"}
        times = ""
        result = {"status": "10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 添加新闻，标题60个汉字,需求范围
    def test_4(self):
        title = ""
        for i in range(30):
            title = title + "测试"
        param = {"title":"测试测试11","username":"18067951267","content":"测试测试","keywords":"测试","description":"test"}
        param["title"] = title 
        pic = {"thumb":"F:\\aaa.jpg"}
        times = ""
        result = {"status": "1004", "message": "[title] This value is too long. It should have 60 characters or less."}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 添加新闻，正文内容为空
    def test_5(self):
        param = {"title":"测试测试11","username":"18067951267","content":"","keywords":"测试","description":"test"}
        pic = {"thumb":"F:\\aaa.jpg"}
        times = ""
        result = {"status": "1004", "message": "[content] 内容不能为空"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 添加新闻，标题使用空格
    def test_6(self):
        param = {"title":"          ","username":"18067951267","content":"测试测试","keywords":"测试","description":"test"}
        pic = {"thumb":"F:\\aaa.jpg"}
        times = ""
        result = {"status": "1004", "message": "[title] This value should not be null."}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 添加新闻，关键次为空
    def test_7(self):
        param = {"title":"测试测试11","username":"18067951267","content":"测试测试","keywords":"","description":"test"}
        pic = {"thumb":"F:\\aaa.jpg"}
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 添加新闻，关键次100个
    def test_8(self):
        keywords = "aaa"
        for i in range(12):
            keywords = keywords+"，"+"".join(random.sample('0123456789abcdef', random.randint(1,5)))
        param = {"title":"测试测试11","username":"18067951267","content":"测试测试","keywords":"测试","description":"test"}
        param["keywords"] = keywords
        pic = {"thumb":"F:\\aaa.jpg"}
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
     
    # 添加新闻，单个关键词15个字
    def test_9(self):
        param = {"title":"测试测试11","username":"18067951267","content":"测试测试","keywords":"aaasssdddfffggg","description":"test"}
        pic = {"thumb":"F:\\aaa.jpg"}
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 添加新闻，摘要内容为空
    def test_10(self):
        param = {"title":"测试测试11","username":"18067951267","content":"测试测试","keywords":"测试","description":""}
        pic = {"thumb":"F:\\aaa.jpg"}
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 添加新闻，摘要内容250字符
    def test_11(self):
        description = ""
        for i in range(250):
            description = description+"".join(random.sample('0123456789abcdef', 1))
        param = {"title":"测试测试11","username":"18067951267","content":"测试测试","keywords":"测试","description":""}
        param["description"] = description
        pic = {"thumb":"F:\\aaa.jpg"}
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 添加新闻，摘要内容251字符,超最长限制
    def test_12(self):
        description = ""
        for i in range(271):
            description = description+"".join(random.sample('0123456789abcdef', 1))
        param = {"title":"测试测试11","username":"18067951267","content":"测试测试","keywords":"测试","description":""}
        param["description"] = description
        pic = {"thumb":"F:\\aaa.jpg"}
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    
    # 添加新闻，不传图片
    def test_13(self):
        param = {"title":"测试测试11","username":"18067951267","content":"测试测试","keywords":"测试","description":"test"}
        pic = ""
        times = ""
        result = {"status":"10000"}
        detailData = Interface().interface(self.url, param, pic, times, result)
        detailData["filename"] = sys._getframe().f_code.co_name
        return detailData
    