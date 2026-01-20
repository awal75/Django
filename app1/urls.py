from django.urls import path
from . import views

urlpatterns = [
    path('app-1/',views.app_1,name='app1-view')
]
