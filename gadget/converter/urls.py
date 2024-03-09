from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name ='home'),
    path('metrics/' , views.metrics , name='metrics'),
    path('weights/' , views.weightConversion , name='weights')
]
