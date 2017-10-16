# _*_ coding: utf-8 _*_
__author__ = 'FWJ'
__date__ = 2017 / 8 / 9
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.models import Admin


class LoginForm(FlaskForm):
    """管理员登录表单"""
    account = StringField(
        label="账号",
        # 验证器（显示错误信息内容）
        validators=[
            DataRequired("请输入账号！")
        ],
        # 描述
        description="账号",
        # 附加选项
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号！",
            # html默认错误信息
            # "required": "required"
        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("请输入密码！")
        ],
        description='密码',
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码！",
            # "required": "required"
        }
    )
    submit = SubmitField(
        '登录',
        render_kw={
            "class": "btn btn-primary btn-block btn-flat",
        }
    )

    # 验证账号
    def validate_account(self, field):
        account = field.data
        # 查询用户是否存在，并统计
        admin = Admin.query.filter_by(name=account).count()
        if admin == 0:
            # 触发异常后，后面的代码就不会再执行
            raise ValidationError("账号不存在！")

