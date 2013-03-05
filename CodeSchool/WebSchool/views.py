from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_school(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/welcome_administrator')
    if request.method == 'POST':
        userName = request.POST['userName']
        userPassword = request.POST['userPassword']
        access = authenticate(username=userName, password=userPassword)
        if access is not None:
            if access.is_active:
                login(request, access)
                return HttpResponseRedirect('/welcome_administrator')
            else:
                warning = 'usuario bloqueado'
                return render_to_response('login.html', {'warning':warning}, context_instance = RequestContext(request))
        else:
            warning = 'contrase;a no valida'
            return render_to_response('login.html', {'warning':warning}, context_instance = RequestContext(request))
    else: 
        return render_to_response('login.html', context_instance = RequestContext(request))

@login_required(login_url='/')
def welcome_administrator(request):
    return render_to_response('welcome_administrator.html', context_instance = RequestContext(request))

@login_required(login_url='/')
def logout_school(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/')
def base_administrator(request):
    return render_to_response('base_administrator.html',{'base_administrator':base_administrator}, context_instance=RequestContext(request))

@login_required(login_url='/')
def qualification(request):
    return render_to_response('qualification.html',{'qualification':qualification}, context_instance=RequestContext(request))
