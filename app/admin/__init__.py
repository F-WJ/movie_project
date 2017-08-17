# _*_ coding: utf-8 _*_
__author__ = 'FWJ'
__date__ = 2017 / 8 / 9
from flask import Blueprint

admin = Blueprint("admin", __name__)

import app.admin.views
