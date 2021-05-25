
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/<int:id>',views.shopInfo,name='shopInfo'),
    
]