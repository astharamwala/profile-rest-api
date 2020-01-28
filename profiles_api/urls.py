"""profiles_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

route = DefaultRouter()
route.register("hello-vs", views.HelloViewset, basename="hello-vs")
route.register("UserProfile", views.UserProfileViewset)
route.register("demo", views.DemoViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello_api', views.HelloApiView.as_view()),
    path('', include(route.urls)),
]
