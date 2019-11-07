#encoding:utf-8

from django.shortcuts import render
from django.views.generic import View
import datetime

class Index(View):
    TEMPLATE = 'index.html'

    def get(self, request, name):
        data = {}
        data['name'] = name
        data['array'] = range(10)
        data['count'] = 20
        data['date'] = datetime.datetime.now()
        data['cut_str'] = 'hello-boy'
        data['first_big'] = 'hello gril'
        data['result'] = None
        data['dic_list'] =  [{'name': 'ty', 'age' :30}, {'name':'ds','age':12}]
        data['float_num'] = 3.1415926
        data['html_str'] = '<div style="background-color:red;width:50px;height:50px"></div>'
        data['a_str'] = '请看 www.baidu.com'
        data['feature'] = data['date'] + datetime.timedelta(days=5)
        return render(request, self.TEMPLATE, data)