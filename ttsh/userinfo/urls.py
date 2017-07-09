from django.conf.urls import url
import views

urlpatterns = [
    url(r'^login/$',views.login),
    url(r'^register/$',views.register),
    url(r'^user_center_info/$',views.user_center_info),
    url(r'^user_center_order/$',views.user_center_order),
    url(r'^user_center_site/$',views.user_center_site),
    url(r'^register_handle/$',views.register_handle),
    url(r'^login_handle/$',views.login_handle),
    # url(r'^$',views.index),
    url(r'^quit_login/$',views.quit_login),
]
