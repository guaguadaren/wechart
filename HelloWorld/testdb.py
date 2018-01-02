# -*- coding: utf-8 -*-
from django.http import HttpResponse
from TestModel.models import Test
# 数据库操作
def adds(request):
    test1 = Test(u_name='阿瓜',u_pwd='123456')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")