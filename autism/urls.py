from django.urls import path
from . import views

app_name='autism'
urlpatterns=[
    path('',views.index,name='index'),
    path("upload", views.upload, name="upload")
]
