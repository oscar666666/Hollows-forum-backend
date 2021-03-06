"""Hollows_forum_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path
from Login import views
#from Register import views
#from Thread import views

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
#router.register(r'post_thread', views.post_thread)
#router.register(r'creat_communities', views.creat_communities)
urlpatterns = [
    path('', include(router.urls)),
    path('Login/', include('Login.urls')),
    path('Register/', include('Register.urls')),
    path('Thread/', include('Thread.urls')),
    path('creat_communities', views.creat_communities),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
