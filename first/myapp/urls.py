from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),  # 127.0.0.1:8000/myapp
    path('about/', views.about, name='about'),  # 127.0.0.1:8000/myapp/about
    path('info/', views.info, name='info'),  # 127.0.0.1:8000/myapp/info
]
