#coding:utf-8
from django.views.generic import View
from django.http import HttpResponse

class TestOne(View):
    def get(self, request,message):
        # message = request.GET.get('message','')
        return HttpResponse('{0}ok'.format(message))