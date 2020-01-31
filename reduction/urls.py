from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),

    url(r'^(?P<short_id>\w{6})$', views.redirect_original_url, name='redirect_original_url'),

    url(r'^makeshort/$', views.shorten_url, name='shorten_url')
]