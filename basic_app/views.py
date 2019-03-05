from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context_dict ={
                    'got':'winter is coming','num':624,
                }
    return render(request,'basic_app/index.html',context_dict)

def base(request):
    return render(request,'basic_app/base.html')

def relative(request):
    return render(request,'basic_app/realtive_url_templates.html')

def other(request):
    return render(request,'basic_app/other.html')

