from django.conf.urls import url
from .import views
urlpatterns=[
    url(r'^$',views.list),
    url(r'^(?P<id>\d+)/$',views.detailpost,name='detailpost'),
]