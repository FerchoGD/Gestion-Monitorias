from django.urls import path
from .views import Home


urlpatterns = [
    # paths del core
    path('',Home.as_view(), name="home"),

]
