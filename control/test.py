#coding=gbk
import os,sys
import importlib
import userBehavior

if __name__ == '__main__':
    module = importlib.import_module("userBehavior.Login")
    print module
    print getattr(module, "Login")
    module.Login().do_work()