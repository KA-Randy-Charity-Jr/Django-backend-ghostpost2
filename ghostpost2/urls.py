"""ghostpost2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from rest_framework import routers
from api import views as api_views
from ghostpost_app import views as ghost_views

router= routers.DefaultRouter()
router.register(r"ghostpost",api_views.GhostViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('api/ghostpost/vote/<int:id>',api_views.vote),
    path('api/boasts/',api_views.BoastView),
    path('api/roasts/',api_views.RoastView)
]
