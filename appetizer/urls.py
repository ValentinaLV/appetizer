"""appetizer URL Configuration

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
from django.urls import path
from appetizer.views import home_page, blog, contact_us, reservation, menu, about_us, catering

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home_page'),
    path('blog/', blog, name='blog_url'),
    path('contact/', contact_us, name='contact_url'),
    path('reservation/', reservation, name='reservation_url'),
    path('menu/', menu, name='menu_url'),
    path('about-us/', about_us, name='about_url'),
    path('catering/', catering, name='catering_url'),
    #path('catering/', include('catering.urls')),
]
