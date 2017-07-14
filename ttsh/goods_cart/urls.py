from django.conf.urls import url
import views
urlpatterns = [
    url(r'^$',views.cart),
    url(r'^add_goods/$',views.add_goods),
    url(r'^get_cart_count/$',views.get_cart_count),
    url(r'^cart_delete/$',views.cart_delete),
    url(r'^cart_edit/$',views.cart_edit),
    url(r'^order/$',views.order),
]