from django.urls import path
from django.views.generic import RedirectView

from mobile import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<alias>/', views.category, name='category'),
    path('<alias>/p/<page>', views.category, name='category_page'),
    path('favicon.ico', RedirectView.as_view(url='/static/image/favicon.ico')),
    path('<alias>/<id>.html', views.aritlce, name='article'),
]
