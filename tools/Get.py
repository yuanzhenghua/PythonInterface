#coding=utf-8
import urllib, urllib2, poster, httplib
import json
import sys, os, random
import subprocess
#stdi,stdo,stde=sys.stdin,sys.stdout,sys.stderr
#reload(sys)
#sys.stdin,sys.stdout,sys.stderr=stdi,stdo,stde
#sys.setdefaultencoding('utf8')


class Get():
    
    def get(self, url):
        try:
            rs =  urllib2.urlopen(url)
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