from django.urls import path
from newapp import views

urlpatterns = [
    path("",views.car_list, name='car_list'),
]