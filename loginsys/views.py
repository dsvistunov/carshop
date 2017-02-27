from django.shortcuts import render, render_to_response, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = 'User not exist'
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')

def regist(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm
    if request.POST:
        new_usr_form = UserCreationForm(request.POST)
        if new_usr_form.is_valid():
            new_usr_form.save()
            new_usr = auth.authenticate(username=new_usr_form.cleaned_data['username'], password=new_usr_form.cleaned_data['password1'])
            auth.login(request, new_usr)
            return redirect('/')
        else:
            args['form'] = new_usr_form
    return render_to_response('regist.html', args)