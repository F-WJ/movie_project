# _*_ coding: utf-8 _*_
__author__ = 'FWJ'
__date__ = 2017 / 8 / 9
from flask import Blueprint
# 定义蓝图
home = Blueprint("home", __name__)

import app.home.views
