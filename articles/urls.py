from django.conf.urls import url
from . import views
from django.urls.conf import path, include
from .router import router

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name="list"),
    path('create/', views.article_create, name="create"),
    path('<slug:slug>/', views.article_detail, name="detail"),
    path('apiarticles/',include(router.urls)),
]
