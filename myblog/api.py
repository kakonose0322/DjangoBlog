from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework.response import Response
from myblog.models import Topmenu,Banner
# 用户管理
from django.contrib.auth.models import User
from django.contrib.auth import login

class TopmenuXuliehua(serializers.ModelSerializer):
    class Meta:
        depath = 1
        model = Topmenu
        fields = '__all__'

class BannerData(serializers.ModelSerializer):
    class Meta:
        depth = 1 #数据深度为1.现在没用到，后续一定会用到，它关系到数据和数据的关联，第一个数据表与第二个数据表是否有关联性，还会拓展到第三个，如果这里存在关联，那么在获取的到这个数据的时候，会将所有有关联的数据都获取到，1 -- 只能获取当前；2 -- 获取与它关联的第一个表
        model = Banner
        fields = ['img'] # 有时候涉及到用户隐私，或者我们不想公示的字段，在不设置的时候会都被请求到。(这里是元组要用[])

@api_view(['GET','POST'])
def indexData(request):
    print('ok')
    topmenu = Topmenu.objects.all()
    topmenuData = TopmenuXuliehua(topmenu,many=True)
    banner = Banner.objects.all()
    bannerData = BannerData(banner,many=True)
    if request.method == 'POST':
        print('ok')
    return Response({'topmenu':topmenuData.data,'banner':bannerData.data})