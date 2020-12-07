from django.urls import path
from . import views
from csvs import views as csvs_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('upload/', csvs_views.upload_file_view, name='upload'),
    path('search/', views.search, name='search'),
]
