from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^addtask/$', views.addtask),
    url(r'^deletetask/$', views.deletetask),
]