from django.test import TestCase
from .views import *


class UrlShortener(TestCase):
    def test_recover_original_url(self):
        url = 'https://www.google.com'
        rec_url = URL(url=url)
        self.assertEqual(url, str(rec_url))

    def test_short_code_duplication(self):
        url = 'https://www.google.com'
        rec_url = URL(url=url)
        sc = shorten_url(rec_url.short_id)
        self.assertEqual(rec_url.short_id, sc)