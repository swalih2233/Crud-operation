from django.urls import path

from product import views

app_name = "product"
urlpatterns = [
     path("",views.index, name="index"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/",views.logout, name="logout"),



    path("product/add/", views.product_add, name="product_add"),
    path("product/delete/<int:id>/",views.product_del, name="product_del"),
    path("product/edit/<int:id>/", views.product_edit, name="product_edit"),

]