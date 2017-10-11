from __future__ import unicode_literals
import os
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.utils.encoding import smart_str
import youtube_dl

def converter(request):
    return render(request, 'index.html', locals())

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(id)s',
    'noplaylist' : True,
    'progress_hooks': [my_hook],
}

def download(request):
    response = HttpResponseRedirect('/')
    if 'url' in request.GET:
        url = request.GET['url']
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(
                url,
                download=False
            )