from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.main_news, name="main_news"),
    path('create', views.create, name="create"),
    path('<int:pk>', views.NewsDetailView.as_view(),name="news_detail"),
    #'<int:pk>' указывает на то что у нас после /news/ будет динамический адресс по типу /news/2 or /news/1 or /news/1231
    path('<int:pk>/update', views.NewsUpdateView.as_view(),name="news_up"),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(),name="news_del")

]