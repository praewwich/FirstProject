from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index',views.index,name='index'),
    url(r'^home/',views.home,name='home'),
    url(r'^add/$',views.add,name='add'),
    url(r'^edit/(?P<pk>\d+)/$',views.edit,name='edit'),
    url(r'^delete/(?P<pk>\d+)/$',views.delete,name='delete'),
]