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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from appetizer.views import home_page, blog, contact_us, about_us, catering

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home_page'),
    path('meals/', include(('meals.urls', 'meals'), namespace='meals')),
    path('reservation/', include(('reservation.urls', 'reservation'), namespace='reservation')),


    path('blog/', blog, name='blog_url'),
    path('contact/', contact_us, name='contact_url'),
    #path('reservation/', reservation, name='reservation_url'),
    # path('menu/', menu, name='menu_url'),
    path('about-us/', about_us, name='about_url'),
    path('catering/', catering, name='catering_url'),
    #path('catering/', include('catering.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
