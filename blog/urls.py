from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('blog/', views.post_list, name='post_list'),
    path('acads/', views.acads, name='acads'),
]
