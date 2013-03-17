from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from WebSchool.models import Course
from CodeSchool.forms import CourseForm
from WebSchool.models import Goal
from CodeSchool.forms import GoalForm
from WebSchool.models import Grade
from CodeSchool.forms import GradeForm
from WebSchool.models import School
from WebSchool.models import Headquarter
from CodeSchool.forms import HeadquarterForm
from WebSchool.models import Score
from CodeSchool.forms import ScoreForm
from WebSchool.models import Student
from CodeSchool.forms import StudentForm
from WebSchool.models import Subject
from CodeSchool.forms import SubjectForm
from WebSchool.models import Teacher
from CodeSchool.forms import TeacherForm


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
def logout_school(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/')
def welcome_administrator(request):
    return render_to_response('welcome_administrator.html', context_instance = RequestContext(request))

@login_required(login_url='/')
def base_administrator(request):
    return render_to_response('base_administrator.html',{'base_administrator':base_administrator}, context_instance=RequestContext(request))

@login_required(login_url='/')
def courses(request):
    courses_list = Course.objects.all()
    return render_to_response('courses.html',{'courses':courses_list}, context_instance=RequestContext(request))

@login_required(login_url='/')
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            courses_list = Course.objects.all()
            return render_to_response('courses.html',{'courses':courses_list}, context_instance=RequestContext(request)) 
    else:
        form = CourseForm()
    return render_to_response('courses.html', {'form':form}, context_instance = RequestContext(request))

@login_required(login_url='/')
def edit_course(request, id_course):
    course = Course.objects.get(pk = id_course)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance = course)
        if form.is_valid():
            form.save()
            courses_list = course.objects.all()
            return render_to_response('courses.html',{'courses':courses_list}, context_instance=RequestContext(request))
    else:
        form = CourseForm(instance = course)
    return render_to_response('courses.html', {'form':form}, context_instance = RequestContext(request))

@login_required(login_url='/')
def delete_course(request, id_course):
    course = Course.objects.get(pk = id_course)
    course.delete()
    courses_list = course.objects.all()
    return render_to_response('courses.html',{'courses':courses_list}, context_instance=RequestContext(request))

@login_required(login_url='/')
def goals(request):
    goals_list = Goal.objects.all()
    return render_to_response('goals.html',{'goals':goals_list}, context_instance=RequestContext(request))

@login_required(login_url='/')
def add_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            form.save()
            goals_list = Goal.objects.all()
            return render_to_response('goals.html',{'goals':goals_list}, context_instance=RequestContext(request)) 
    else:
        form = GoalForm()
    return render_to_response('goals.html', {'form':form}, context_instance = RequestContext(request))

@login_required(login_url='/')
def edit_goal(request, id_Goal):
    goal = Goal.objects.get(pk = id_Goal)
    if request.method == 'POST':
        form = GoalForm(request.POST, instance = Goal)
        if form.is_valid():
            form.save()
            goals_list = Goal.objects.all()
            return render_to_response('goals.html',{'goals':goals_list}, context_instance=RequestContext(request))
    else:
        form = GoalForm(instance = goal)
    return render_to_response('goals.html', {'form':form}, context_instance = RequestContext(request))

@login_required(login_url='/')
def delete_goal(request, id_Goal):
    goal = Goal.objects.get(pk = id_Goal)
    goal.delete()
    goals_list = Goal.objects.all()
    return render_to_response('Goals.html',{'Goals':goals_list}, context_instance=RequestContext(request))


@login_required(login_url='/')
def grades(request):
    grades_list = Grade.objects.all()
    return render_to_response('grades.html',{'grades':grades_list}, context_instance=RequestContext(request))

@login_required(login_url='/')
def add_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            grades_list = Grade.objects.all()
            return render_to_response('grades.html',{'grades':grades_list}, context_instance=RequestContext(request)) 
    else:
        form = GradeForm()
    return render_to_response('grades.html', {'form':form}, context_instance = RequestContext(request))

@login_required(login_url='/')
def edit_grade(request, id_grade):
    grade = Grade.objects.get(pk = id_grade)
    if request.method == 'POST':
        form = GradeForm(request.POST, instance = grade)
        if form.is_valid():
            form.save()
            grades_list = grade.objects.all()
            return render_to_response('grades.html',{'grades':grades_list}, context_instance=RequestContext(request))
    else:
        form = GradeForm(instance = grade)
    return render_to_response('grades.html', {'form':form}, context_instance = RequestContext(request))

@login_required(login_url='/')
def delete_grade(request, id_grade):
    grade = Grade.objects.get(pk = id_grade)
    grade.delete()
    grades_list = grade.objects.all()
    return render_to_response('grades.html',{'grades':grades_list}, context_instance=RequestContext(request))

@login_required(login_url='/')
def headquarters(request):
    headquarters_list = Headquarter.objects.all()
    return render_to_response('headquarters.html',{'headquarters':headquarters_list}, context_instance=RequestContext(request))

@login_required(login_url='/')
def add_headquarter(request):
    if request.method == 'POST':
        form = HeadquarterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/headquarters') 
    else:
        form = HeadquarterForm()
    return render_to_response('headquarters.html', {'form':form}, context_instance = RequestContext(request))

@login_required(login_url='/')
def edit_headquarter(request, id_headquarter):
    headquarter = School.objects.get(pk = id_headquarter)
    if request.method == 'POST':
        form = HeadquarterForm(request.POST, instance = headquarter)
        if form.is_valid():
            form.save()
            headquarters_list = headquarter.objects.all()
            return render_to_response('headquarters.html',{'headquarters':headquarters_list}, context_instance=RequestContext(request))
    else:
        form = HeadquarterForm(instance = headquarter)
    return render_to_response('headquarters.html', {'form':form}, context_instance = RequestContext(request))

@login_required(login_url='/')
def delete_headquarter(request, id_headquarter):
    headquarter = School.objects.get(pk = id_headquarter)
    headquarter.delete()
    headquarters_list = headquarter.objects.all()
    return render_to_response('headquarters.html',{'headquarters':headquarters_list}, context_instance=RequestContext(request))


@login_required(login_url='/')
def qualifications(request):
    qualifications_list = Score.objects.all()
    return render_to_response('qualifications.html',{'qualifications':qualifications_list}, context_instance=RequestContext(request))

@login_required(login_url='/')
def add_qualification(request):
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            form.save()
            qualifications_list = Score.objects.all()
            return render_to_response('qualifications.html',{'qualifications':qualifications_list}, context_instance=RequestContext(request)) 
    else:
        form = ScoreForm()
    return render_to_response('qualifications.html', {'form':form}, context_instance = RequestContext(request))

@login_required(login_url='/')
def edit_qualification(request, id_qualification):
    qualification = Score.objects.get(pk = id_qualification)
    if request.method == 'POST':
        form = ScoreForm(request.POST, instance = qualification)
        if form.is_valid():
            form.save()
            qualifications_list = qualification.objects.all()
            return render_to_response('qualifications.html',{'qualifications':qualifications_list}, context_instance=RequestContext(request))
    else:
        form = ScoreForm(instance = qualification)
    return render_to_response('qualifications.html', {'form':form}, context_instance = RequestContext(request))

@login_required(login_url='/')
def delete_qualification(request, id_qualification):
    qualification = Score.objects.get(pk = id_qualification)
    qualification.delete()
    qualifications_list = qualification.objects.all()
    return render_to_response('qualifications.html',{'qualifications':qualifications_list}, context_instance=RequestContext(request))

@login_required(login_url='/')
def students(request, state):
    students_list = []
    state_selected = ''
    if state == '0':
        students_list = Student.objects.filter(student_matriculated = False)
        state_selected = '0'
    elif state == '1':
        students_list = Student.objects.filter(student_matriculated = True)
        state_selected = '1'
    elif state == '2':
        students_list = Student.objects.all()
        state_selected = '2'
    return render_to_response('students.html',{'students':students_list, 'state_selected':state_selected}, context_instance=RequestContext(request))

@login_required(login_url='/')
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/2') 
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
            return HttpResponseRedirect('/students/2')
    else:
        form = StudentForm(instance = student)
    return render_to_response('students.html', {'form':form}, context_instance = RequestContext(request))

@login_required(login_url='/')
def delete_student(request, id_student):
    student = Student.objects.get(pk = id_student)
    student.delete()
    return HttpResponseRedirect('/students/2')

@login_required(login_url='/')
def subjects(request):
    subjects_list = Subject.objects.all()
    return render_to_response('subjects.html',{'subjects':subjects_list}, context_instance=RequestContext(request))

@login_required(login_url='/')
def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            subjects_list = Subject.objects.all()
            return render_to_response('subjects.html',{'subjects':subjects_list}, context_instance=RequestContext(request)) 
    else:
        form = SubjectForm()
    return render_to_response('subjects.html', {'form':form}, context_instance = RequestContext(request))

@login_required(login_url='/')
def edit_subject(request, id_subject):
    subject = Subject.objects.get(pk = id_subject)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance = subject)
        if form.is_valid():
            form.save()
            subjects_list = subject.objects.all()
            return render_to_response('subjects.html',{'subjects':subjects_list}, context_instance=RequestContext(request))
    else:
        form = SubjectForm(instance = subject)
    return render_to_response('subjects.html', {'form':form}, context_instance = RequestContext(request))

@login_required(login_url='/')
def delete_subject(request, id_subject):
    subject = Subject.objects.get(pk = id_subject)
    subject.delete()
    subjects_list = subject.objects.all()
    return render_to_response('subjects.html',{'subjects':subjects_list}, context_instance=RequestContext(request))

@login_required(login_url='/')
def teachers(request):
    teachers_list = Teacher.objects.all()
    return render_to_response('teachers.html',{'teachers':teachers_list}, context_instance=RequestContext(request))

@login_required(login_url='/')
def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            teachers_list = Teacher.objects.all()
            return render_to_response('teachers.html',{'teachers':teachers_list}, context_instance=RequestContext(request)) 
    else:
        form = TeacherForm()
    return render_to_response('teachers.html', {'form':form}, context_instance = RequestContext(request))

@login_required(login_url='/')
def edit_teacher(request, id_teacher):
    teacher = Teacher.objects.get(pk = id_teacher)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance = teacher)
        if form.is_valid():
            form.save()
            teachers_list = teacher.objects.all()
            return render_to_response('teachers.html',{'teachers':teachers_list}, context_instance=RequestContext(request))
    else:
        form = TeacherForm(instance = teacher)
    return render_to_response('teachers.html', {'form':form}, context_instance = RequestContext(request))

@login_required(login_url='/')
def delete_teacher(request, id_teacher):
    teacher = Teacher.objects.get(pk = id_teacher)
    teacher.delete()
    teachers_list = teacher.objects.all()
    return render_to_response('teachers.html',{'teachers':teachers_list}, context_instance=RequestContext(request))


@login_required(login_url='/')
def reports(request):
    return render_to_response('reports.html',{'reports':reports}, context_instance=RequestContext(request))

@login_required(login_url='/')
def school(request):
    return render_to_response('school.html',{'school':school}, context_instance=RequestContext(request))

@login_required(login_url='/')
def school_year(request):
    warning = 'Html en mantenimiento'
    return render_to_response('school.html', {'warning':warning}, context_instance = RequestContext(request))