#coding:utf-8
from django.views.generic import View
from django.shortcuts import render,redirect,reverse
from .contents import MessageType
from .models import Message
from .forms import MessageForm
import time

class Three(View):
    TEMPLATE = 'three.html'
    def get(self, request, message_type):
        data = {}
        try:
            message_type_obj = MessageType[message_type]
        except Exception as e:
            data['error'] = '没有这个消息类型{}'.format(e)
            return render(request, self.TEMPLATE, data)

        message = request.GET.get('message', '')

        if not message:
            data['error'] = '消息不能为空'
            return render(request, self.TEMPLATE, data)


        data['message'] = message
        data['message_type'] = message_type_obj

        return render(request, self.TEMPLATE, data)

class FourPageOne(View):
    TEMPLATE = 'FourPageOne.html'
    def get(self, request, message_type):
        data = {}
        try:
            message_type_obj = MessageType[message_type]
        except Exception as e:
            data['error'] = '没有这个消息类型{}'.format(e)
            return render(request, self.TEMPLATE, data)

        message = request.GET.get('message', '')

        if not message:
            data['error'] = '消息不能为空'
            return render(request, self.TEMPLATE, data)


        data['message'] = message
        data['message_type'] = message_type_obj

        Message.objects.create(content = message,
                               message_type = message_type_obj.value,
                               create_time = time.time())


        return redirect(reverse('fourpagetwo'))

class FourPageTwo(View):
    TEMPLATE = 'FourPageTwo.html'
    def get(self,request):
        data = {}
        search = request.GET.get("search" , '')
        if not search:
            messages = Message.objects.all()

        else:
            messages = Message.objects.filter(content__contains=search)
        data['messages'] = messages
        return render(request, self.TEMPLATE, data)

# delete message using id
class FourPageThree(View):
    def get(self, requset):
        id = requset.GET.get('id', '')
        message_obj = Message.objects.get(id=id)
        message_obj.delete()
        return redirect(reverse("fourpagetwo"))


class FourPageFour(View):
    def get(self, request):
        id = request.GET.get("id" , '')
        message = request.GET.get('message','')

        message_obj = Message.objects.get(id=id)
        message_obj.content = message
        message_obj.save()

        return redirect(reverse("fourpagetwo"))

class FivePage(View):
    TEMPLATE = 'five.html'
    def get(self, request):
        data = {}
        data['form'] = MessageForm()

        return render(request, self.TEMPLATE, data)

    def post(self,request):
        form = MessageForm(request.POST)

        if form.is_valid():
            message = form.cleaned_data.get('content')
            message_type_obj = form.cleaned_data.get("message_type")
            Message.objects.create(content=message,
                                   message_type=message_type_obj.value,
                                   create_time=time.time())

        else:
            return render(request, self.TEMPLATE, {"form": form})
        return redirect(reverse('fourpagetwo'))
