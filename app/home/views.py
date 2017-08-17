# _*_ coding: utf-8 _*_
__author__ = 'FWJ'
__date__ = 2017 / 8 / 9
from . import home


# 调用蓝图
@home.route("/")
def index():
    return "<h1 style='color:green'>this is home</h1>"
