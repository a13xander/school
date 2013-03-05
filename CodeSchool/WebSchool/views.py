from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

def login_school(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        userName = request.POST['userName']
        userPassword = request.POST['userPassword']
        access = authenticate(username=userName, password=userPassword)
        if access is not None:
            if access.is_active:
                login(request, access)
                return HttpResponseRedirect('/welcome_administrator')
            else:
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    else: 
        return render_to_response('login.html', context_instance = RequestContext(request))

def welcome_administrator(request):
    return render_to_response('welcome_administrator.html', context_instance = RequestContext(request))

def base_administrator(request):
    return render_to_response('base_administrator.html',{'base_administrator':base_administrator}, context_instance=RequestContext(request))

def qualification(request):
    return render_to_response('qualification.html',{'qualification':qualification}, context_instance=RequestContext(request))
