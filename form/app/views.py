from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from .forms import Auth


class Register(View):
    TEMPLATE = 'register.html'

    def get(self, request):
        form = Auth()

        return render(request, self.TEMPLATE, {'form' : form})

    def post(self, request):
        form = Auth()
        if form.is_valid():
            usernanme = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print('username: ', usernanme)
            print('password: ', password)
        return redirect(reverse('register'))