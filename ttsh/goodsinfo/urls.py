from django.conf.urls import url
import views
urlpatterns=[
    url(r'^detail(\d+)/$',views.detail),
    url(r'^$',views.index),
    url(r'^list(\d+)_(\d+)_(\d+)/$',views.list),
    url(r'^search/$', views.MySearchView.as_view(), name='search_view'),
]