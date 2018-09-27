from django.shortcuts import render,HttpResponse


def showmsg(request):
    return HttpResponse('my name is kratika')