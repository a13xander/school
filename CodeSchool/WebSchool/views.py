from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from WebSchool.models import Student
from CodeSchool.forms import StudentForm

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
def qualifications(request):
    return render_to_response('qualifications.html',{'qualifications':qualifications}, context_instance=RequestContext(request))

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
def headquarters(request):
    return render_to_response('headquarters.html',{'headquarters':qualifications}, context_instance=RequestContext(request))

@login_required(login_url='/')
def students(request):
    students_list = Student.objects.all()
    return render_to_response('students.html',{'students':students_list}, context_instance=RequestContext(request))

@login_required(login_url='/')
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            students_list = Student.objects.all()
            return render_to_response('students.html',{'students':students_list}, context_instance=RequestContext(request)) 
    else:
        form = StudentForm()
    return render_to_response('students.html', {'form':form}, context_instance = RequestContext(request))

@login_required(login_url='/')
def edit_student(request, id_student):
    student = Student.objects.get(pk = id_student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance = student)
        if form.is_valid():
            form.save()
            students_list = Student.objects.all()
            return render_to_response('students.html',{'students':students_list}, context_instance=RequestContext(request))
    else:
        form = StudentForm(instance = student)
    return render_to_response('students.html', {'form':form}, context_instance = RequestContext(request))

@login_required(login_url='/')
def delete_student(request, id_student):
    student = Student.objects.get(pk = id_student)
    student.delete()
    students_list = Student.objects.all()
    return render_to_response('students.html',{'students':students_list}, context_instance=RequestContext(request))