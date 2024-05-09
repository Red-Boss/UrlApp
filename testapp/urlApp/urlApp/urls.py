"""
URL configuration for urlApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from urlCheker import views

urlpatterns = [
    path('', views.url_list, name='url_list'),
    path('check/<int:pk>/', views.check_url, name='check_url'),
    path('check_all/', views.check_all_urls, name='check_all_urls'),
    path('delete/<int:pk>/', views.delete_url, name='delete_url'),
    path('statistics/', views.statistics, name='statistics'),
]
