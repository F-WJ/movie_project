# _*_ coding: utf-8 _*_
__author__ = 'FWJ'
__date__ = 2017 / 8 / 9
from . import admin


# 调用蓝图
@admin.route("/")
def index():
    return "<h1 style='color:red'>this is admin<h1>"
