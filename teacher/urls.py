from django.urls import path
from .views import index,index2

urlpatterns= [
    path("tach",index),
    path('hello',index2)
]