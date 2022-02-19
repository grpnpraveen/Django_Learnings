from django.urls import path
from . import views


urlpatterns = [
    path('', views.TravelloHome,name="TravelloHomePage"),
    path('load', views.TravelloHomePostgres,name="TravelloHomePagePostgres"),
]
