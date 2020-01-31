import random
import string
import json

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from django.shortcuts import render, get_object_or_404

from reduction.models import URL
from reduction.invalid import InvalidGet


def index(request):
    general = {}
    general.update(csrf(request))
    return render(request, 'reduction/index.html')


def shorten_url(request):
    url = request.POST.get('url', '')
    if not (url == ''):
        try:
            url_present = URL.objects.get(url=url)
            short_id = url_present.short_id
        except URL.DoesNotExist:
            short_id = get_short_code()

        n_url = URL(url=url, short_id=short_id)
        n_url.save()

        response_data = {'url': settings.SITE_URL + '/' + short_id}

        return HttpResponse(json.dumps(response_data), content_type="application/json")
    return HttpResponse(json.dumps({'error': 'error occurs'}), content_type="application/json")


def redirect_original_url(request, short_id):
    n_url = get_object_or_404(URL, pk=short_id)
    n_url.counter += 1
    n_url.save()
    return HttpResponseRedirect(n_url.url)


def get_short_code():
    length = 6
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    while True:
        short_id = ''.join(random.choice(char) for _ in range(length))
        try:
            temp = URL.objects.get(pk=short_id)
            return temp
        except InvalidGet:
            return short_id
