import datetime
import time
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .core.api import get_accounts_info, get_insta_content_and_comments, make_access_redirect_link, get_access_code
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from .models import Facebook


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('account'))
    if request.method == 'GET':
        wrong_data = request.GET.get('bad_auth') is not None
        return render(request, 'index.html', {'bad_auth': wrong_data})
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse_lazy('account'))
        else:
            return HttpResponseRedirect(reverse_lazy('index') + '?bad_auth')


def account(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('index'))
    try:
        fb = Facebook.objects.get(user=request.user)
        i = get_accounts_info(fb.access_token)
    except:
        i = None
    return render(request, 'account.html', {'data': i})


def insta_content(request, ig_id):
    fb = Facebook.objects.get(user=request.user)
    i = get_insta_content_and_comments(ig_id, fb.access_token)
    return render(request, 'insta_content.html', {'data': i})


def get_creds(request, user_id):
    return HttpResponseRedirect(make_access_redirect_link(user_id))


def fb_auth(request):
    code = request.GET.get('code')
    x = get_access_code(code)

    fb = Facebook()
    fb.user = request.user
    fb.access_token = x['access_token']
    fb.expires_in = datetime.datetime.now() + datetime.timedelta(seconds=x['expires_in'] - 600)
    fb.save()
    return HttpResponseRedirect('/account/')
