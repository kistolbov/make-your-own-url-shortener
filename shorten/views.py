import random
import string

from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError

from .models import URL
from .forms import URLForm
from .invalid import InvalidRedirectShortURL


def redirect_short_url(request, short_id):
    try:
        url = URL.objects.get(short_id=short_id)
        return redirect(url.url)
    except InvalidRedirectShortURL:
        return render(request, template_name='shorten/404.html')


def get_urls(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            short_id = form.cleaned_data['CustomURL']
            if short_id == '':
                short_id = short_id_generator()
                main_url = form.cleaned_data['MainURL']
                url = URL(url=main_url, short_id=short_id)
                url.save()
                messages.success(request, 'ShortURL was created!')
                return render(request, 'shorten/shorturl_created.html', {'main_url': main_url, 'short_id': short_id})
            else:
                try:
                    url = URL(url=form.cleaned_data['MainURL'], short_id=short_id)
                    url.save()
                    messages.success(request, 'ShortURL was created!')
                    return render(request, 'shorten/shorturl_created.html', {'main_url': form.cleaned_data['MainURL'], 'short_id': short_id})
                except IntegrityError:
                    messages.success(request, 'URL is already taken. Try with different name.')
                    return redirect('home')
        else:
            messages.success(request, "You didn't paste the URL. Try a different input.")
            return redirect('home')

    form = URLForm()
    return render(request, 'shorten/url_short.html', {'form': form})


def short_id_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))