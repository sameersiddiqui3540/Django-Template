from  django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns =[
    url(r'^relative/$',views.relative,name="relative"),
    url(r'^other/$',views.other,name="other"),
    url(r'^base/$',views.base,name="base"),
    url(r'^index/$',views.index,name="index"),
]