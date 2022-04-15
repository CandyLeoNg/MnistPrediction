import json

from django.core.files.base import ContentFile
from django.http.response import HttpResponse
from django.shortcuts import render
from mnist import predict
import matplotlib.pyplot as plt

# 创建Login函数
def Login(request):
    return render(request,'../template/index.html',{
        "result": '待上传图片'
    })


def process(request):
    path = '../mnistPredict/mnistImg/'
    img_path = request.POST.get("file", "")
    pathAll = path + img_path
    pred = predict.Predict(pathAll)
    return render(request,'index.html',{
        "result": pred,
        "url": pathAll
    })
    # 打印输出文件名
