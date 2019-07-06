"""simple_cms URL Configuration

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
from django.urls import path, include
from django.views.generic import RedirectView

from simple_cms import views

urlpatterns = [
    path(r'mobile/', include('mobile.urls')),
    path('sitemap.xml', views.sitemap, name='sitemap'),
    path('sitemap.xsl', views.sitemap_xsl, name='sitemap_xsl'),
    path(r'search/', include('haystack.urls')),
    path('admin/settings/save', views.settings_save),
    path('admin/settings', views.settings),
    path('admin/', admin.site.urls),
    path('ueditor/upload', views.ueditor_upload),
    path('favicon.ico', RedirectView.as_view(url='static/image/favicon.ico')),
    path('', views.index),
    path('topic/', views.category, name='category_all'),
    path('topic/<page>', views.category, name='category_all_page'),
    path('<category_alias>/', views.category, name='category'),
    path('<category_alias>/p/<page>', views.category, name='category_page'),
    path('<category>/<id>.html', views.aritlce, name='article'),

]
