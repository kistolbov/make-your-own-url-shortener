from django.urls import path
from shorten.views import redirect_short_url, get_urls


urlpatterns = [
    path('<short_id>/', redirect_short_url),
    path('', get_urls, name='home')
]