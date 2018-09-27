from django.urls import path
from myapp.views import showmsg

urlpatterns=[
    path('showmsg/',showmsg,name="my name is kratika"),

]