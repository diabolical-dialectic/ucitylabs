from django.conf.urls import url
from main_app import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    # new url definition
    url(r'^contact/$', views.contact, name='contact'),
]
