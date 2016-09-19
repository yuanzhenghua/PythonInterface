#coding=gbk
import time
import json
import os
import xlrd
import sys
#stdi,stdo,stde=sys.stdin,sys.stdout,sys.stderr
#reload(sys)
#sys.stdin,sys.stdout,sys.stderr=stdi,stdo,stde
#sys.setdefaultencoding('gb2312')

class ReadFile():
    def ReadXls(self, path):
        data = {}
        #检查xls文件是否存在
        if not os.path.exists(path):
            return 'I cannot find the "%s" file.'
        #读取数据
        f = xlrd.open_workbook(path)
        table1 = f.sheets()[0]    
        params = []
        for i in range(1, table1.nrows):
            p = ""
            for j in range(table1.ncols):
                k = str(int(table1.cell(0,j).value)) if type(table1.cell(0,j).value)==float else str(table1.cell(0,j).value)
                v = str(int(table1.cell(i,j).value)) if type(table1.cell(i,j).value)==float else str(table1.cell(i,j).value)
                if k == "pic":
                    v = str(open(v).read())
                p = p+'"'+k+'":"'+v+'"'
                if j<table1.ncols-1:
                    p = p+","
            params.append(p)
    
        table2 = f.sheets()[1]
        results = []
        for i in range(1, table2.nrows):
            r = ""
            for j in range(table2.ncols):
                k = str(int(table2.cell(0,j).value)) if type(table2.cell(0,j).value)==float else str(table2.cell(0,j).value)
                v = str(int(table2.cell(i,j).value)) if type(table2.cell(i,j).value)==float else str(table2.cell(i,j).value)
                r = r+'"'+k+'":"'+v+'"'
                if j<table2.ncols-1:
                    r = r+","
            results.append(r)
    
        data["params"] = params
        data["results"] = results
        return data
    
    def ReadXls2(self, path):
        data = []
        #检查xls文件是否存在
        if not os.path.exists(path):
            return 'I cannot find the "%s" file.'
        #读取数据
        f = xlrd.open_workbook(path)
        table = f.sheets()[0]
        for i in range(1, table.nrows):
            p = {}
            for j in range(table.ncols):
                k = str(int(table.cell(0,j).value)) if type(table.cell(0,j).value)==float else str(table.cell(0,j).value)
                v = str(int(table.cell(i,j).value)) if type(table.cell(i,j).value)==float else str(table.cell(i,j).value)
                p[k] = v          
            data.append(p)
        return data
    
    def ReadXls3(self, path, Id):
        data = []
        #检查xls文件是否存在
        if not os.path.exists(path):
            return 'I cannot find the "%s" file.'
        #读取数据
        f = xlrd.open_workbook(path)
        table = f.sheets()[0]
        for i in range(1, table.nrows):
            p = {}
            for j in range(table.ncols):
                k = str(int(table.cell(0,j).value)) if type(table.cell(0,j).value)==float else str(table.cell(0,j).value)
                v = str(int(table.cell(i,j).value)) if type(table.cell(i,j).value)==float else str(table.cell(i,j).value)
                p[k] = v
            if p["id"] == str(Id):
                data.append(p)
        return data

#if __name__ == "__main__":
    #r = ReadXls(os.getcwd()+"\\data\\Login.xls")
    #r = ReadXls3("F:\\E电商文档\\测试用例\\接口测试\\接口测试用例.xlsx", 1)
    #print r
