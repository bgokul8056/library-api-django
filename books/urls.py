from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.funcName.as_view(),name="home"),
]