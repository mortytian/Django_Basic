#coding:utf-8

from django.http import HttpResponse
from django.views.generic import View

class Index(View):
    def get(self, request, name, age):
        print(dir(request))
        return HttpResponse('hello i am {0}, age is {1}'.format(name,age))

# def index(request):
    # name = request.GET.get('name','')
    # age = request.GET.get("age", 0)
    # return HttpResponse('hello i am {0}, age is {1}'.format(name,age))


# def index(resquest,name,age):
#     return HttpResponse('I am {0}, age is {1}'.format(name,age))

