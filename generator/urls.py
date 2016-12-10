from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^generate_image/', views.generate_image, name='generate_image'),
    url(r'^get_image/', views.get_image, name='get_image')
]
