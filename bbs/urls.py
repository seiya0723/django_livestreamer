from django.urls import path
from . import views

app_name    = "bbs"
urlpatterns = [
    path('', views.index, name="index"),
    path('stream/', views.stream, name="stream"),
    path('video_control/', views.video_control, name="video_control"),

]

