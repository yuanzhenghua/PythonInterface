#coding=utf-8
import MySQLdb

class MySQL(object):

    def __init__(self):
        self.host = "120.26.119.42"
        self.port = 3306
        self.user = "root"
        self.pwd = "root"
        self.db = ""
    
    def __GetConnect(self):
        try: 
            self.conn = MySQLdb.connect(host=self.host,port=self.port,user=self.user,passwd=self.pwd,db=self.db)
            cur = self.conn.cursor()   
            if not cur:  
                raise(NameError,"杩炴帴鏁版嵁搴撳け璐�")  
            else:  
                return cur
        except Exception as e:
            print e
  
    def VerifyConnection(self):  
        try:  
            if self.host=='':  
                return ""  
            conn = MySQLdb.connect(host=self.host,port=self.port,user=self.user,passwd=self.pwd,db=self.db)  
            return conn  
        except:  
            return ""  
  
    def ExecQuery(self, db, sql):
        self.db = db
        cur = self.__GetConnect()  
        cur.execute(sql)  
        resList = cur.fetchall()
        self.conn.close()  
        return resList  
  
    def ExecNonQuery(self, db, sql):
        print sql
        self.db = db   
        cur = self.__GetConnect()
        cur.execute(sql)  
        self.conn.commit()  
        self.conn.close()  
