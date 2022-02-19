from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name="HomePage"),
    path('add', views.add,name="ResultPage"),
]
