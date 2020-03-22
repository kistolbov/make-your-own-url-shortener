from django.test import TestCase

from shorten.models import URL
from shorten.views import redirect_short_url, get_urls


class URLShortenerTest(TestCase):
    def check_duplication(self):
        link = URL(url='https://www.google.com/', short_id='cutiepie')
        url = 'https://www.google.com/'
        self.assertEqual(link.url, url)

    def check_redirect_original_url(self):
        redirect_short_url(request='POST', short_id='cutiepie')

    def check_get_url(self):
        get_urls(request='POST')
