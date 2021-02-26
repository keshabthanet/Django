from . import views
from django.urls import path

app_name='blog'
urlpatterns = [
    path('',views.index,name='index'),
    path('detail/<int:blog_id>/',views.detail,name='detail'),
    
]