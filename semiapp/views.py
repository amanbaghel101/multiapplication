from django.shortcuts import render

# Create your views here.
def data_render(request):
    data = 'aman'
    d = {'name':data}
    return render(request,'login.html',context=d)