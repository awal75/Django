from django.urls import path
from . import views

urlpatterns = [
    path('app-3/',views.app_3,name='app3-view')
]
