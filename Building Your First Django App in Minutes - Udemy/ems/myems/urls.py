"""myems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
# from .admin import my_ems_admin_site

# from . import views 

# admin.site.site_header = "Test 1"
# admin.site.site_title = "Test 2"
# admin.site.index_title = "Test 300"

urlpatterns = [
    path('admin/', admin.site.urls), 

    # path('employees/', admin.site.urls),
    # url(r'^admin/', admin.site.urls),
    url(r'^employees/(?P<pk>[0-9]{8})/profile/$', views.my_profile, name='my_profile'),
]
