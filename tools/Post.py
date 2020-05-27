#coding=utf-8
import poster3
import json
from urllib import request
from http import cookiejar

#stdi,stdo,stde=sys.stdin,sys.stdout,sys.stderr
#reload(sys)
#sys.stdin,sys.stdout,sys.stderr=stdi,stdo,stde
#sys.setdefaultencoding('utf8')


class Post():
    
    def post(self, url, param, header, cookie, method):
        print "url=",url
        print "param=",param
        if method == "multipart/form-data":
            ajaxResponse = self.post_multipart_form_data(url, param, header, cookie)
        return ajaxResponse
    
    def post_multipart_form_data(self, url, param, header, cookie, referer=None):
        try:
            poster3.streaminghttp.register_openers()
            datagen, headers = poster3.encode.multipart_encode(param)
            if header <> "":
                for k in header:
                    headers[k] = header[k]
            request = request.Request(url, datagen, headers)
            if cookie<>"":
                cookiejar = cookiejar.CookieJar()
                rs = request.build_opener(request.HTTPCookieProcessor(cookiejar)).urlopen(request).read()
            else:
                rs = request.urlopen(request).read()
            #print "rs=",rs
            if ""<>rs:
                rs = json.loads(rs)
            print "rs=",json.dumps(rs ,ensure_ascii=False)
            return rs
        except Exception as e:
            print "error=",str(e)
            #print "e.code=",e.code
            #print "e.read()=",e.read()
            print
            return ""  

#if __name__ == "__main__":
    #r = post('"url":"http://www.aliwap.cn/api/user/login","_username":"13486119817","_password":"1234567"')
    #request_ajax_url("http://open.aliwap.cn:8000/ad/banner/get_banner_list", "")
