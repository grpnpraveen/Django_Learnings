from django.urls import path
from . import views


urlpatterns = [
    path('register', views.AccountsRegister,name="AccountsRegister"),
    path('login', views.AccountsLogin,name="AccountsLogin"),
    path('logout', views.AccountsLogout,name="AccountsLogout"),

]
