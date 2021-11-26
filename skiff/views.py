from django.shortcuts import render, get_object_or_404
from django.http import Http404
from skiff.models import *
from skifftest.settings import STATICFILES_DIRS

def index(request):
    s_user_list = s_user.objects.all()
    context = {'s_user_list': s_user_list}
    return render(request, 'index.html', context)


