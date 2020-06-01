from django.shortcuts import render
from .models import Topmenu

# Create your views here.
# 将请求带回
def index(request):
    topmenu = Topmenu.objects.all()
    context = {
        'topmenu':topmenu
    }
    return render(request,'index.html',context)
