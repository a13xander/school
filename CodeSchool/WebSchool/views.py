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
        print(request.POST)
#        if request.POST['rememberMe']== 'True':
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
def qualifications(request):
    return render_to_response('qualification.html',{'qualifications':qualifications}, context_instance=RequestContext(request))

@login_required(login_url='/')
def subjects(request):
    return render_to_response('subjects.html',{'subjects':subjects}, context_instance=RequestContext(request))

@login_required(login_url='/')
def teachers(request):
    return render_to_response('teachers.html',{'teachers':teachers}, context_instance=RequestContext(request))

@login_required(login_url='/')
def reports(request):
    return render_to_response('reports.html',{'reports':reports}, context_instance=RequestContext(request))

@login_required(login_url='/')
def goals(request):
    return render_to_response('goals.html',{'goals':goals}, context_instance=RequestContext(request))

@login_required(login_url='/')
def grades(request):
    return render_to_response('grades.html',{'grades':grades}, context_instance=RequestContext(request))

@login_required(login_url='/')
def courses(request):
    return render_to_response('courses.html',{'courses':courses}, context_instance=RequestContext(request))

@login_required(login_url='/')
def students(request):
    return render_to_response('students.html',{'students':qualifications}, context_instance=RequestContext(request))

@login_required(login_url='/')
def headquarters(request):
    return render_to_response('headquarters.html',{'headquarters':qualifications}, context_instance=RequestContext(request))
