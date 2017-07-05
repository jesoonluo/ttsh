from django.conf.urls import url
import views

urlpatterns = [
    url(r'^login/$',views.login),
    url(r'^register/$',views.register),
    url(r'^user_center_info/$',views.user_center_info),
]