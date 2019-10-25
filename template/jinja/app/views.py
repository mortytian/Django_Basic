from django.shortcuts import render

# Create your views here.

def test(request):
    data = {'name' :'ef', 'age' : 12}
    return render(request,'test.html', data)
