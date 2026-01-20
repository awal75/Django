from django.urls import path
from . import views

urlpatterns = [
    path('app-2/',views.app_2,name='app2-view')
]
