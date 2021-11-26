from django.shortcuts import render
from django.http import HttpResponseRedirect
from skifftest.settings import BASE_DIR
from .forms import *
from skiff.models import *

def err_404_view(request, exception):
    return render(request, '404.html', status = 404)

def landing(request):
    return render(request, 'home.html')

def auth(request):
    if request.method == 'POST':
        form = S_UserAuthForm(request.POST)

        if form.is_valid():
            out_user = s_user.objects.filter(name = form.cleaned_data['user_name'])

            if out_user:
                if out_user.filter( password = form.cleaned_data['user_password']):
                    context = { 'form': form,
                                'name_msg': True,
                                'password_msg': True}
                    return HttpResponseRedirect('/home/')
                else:
                    context = { 'form': form,
                                'name_msg': True,
                                'password_msg': False}
                
            else:
                context = { 'form': form,
                            'name_msg': False,
                            'password_msg': False}
            
    else:
        form = S_UserAuthForm()
        context = { 'form': form,
                    'name_msg': False,
                    'password_msg': False}

    return render(request, 'auth.html', context)