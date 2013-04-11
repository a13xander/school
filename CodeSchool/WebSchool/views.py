#encoding:utf-8

from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from WebSchool.models import Course, Course_history, Allocation
from CodeSchool.forms import CourseForm
from WebSchool.models import Goal
from CodeSchool.forms import GoalForm
from WebSchool.models import Grade
from CodeSchool.forms import GradeForm
from WebSchool.models import Headquarter
from CodeSchool.forms import HeadquarterForm
from WebSchool.models import School
from CodeSchool.forms import SchoolForm
from WebSchool.models import Score
from CodeSchool.forms import ScoreForm
from WebSchool.models import Student
from CodeSchool.forms import StudentForm
from WebSchool.models import Subject
from CodeSchool.forms import SubjectForm
from WebSchool.models import Teacher
from CodeSchool.forms import TeacherForm
from WebSchool.models import Year
from django.db.models.deletion import ProtectedError


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
    year = School.objects.filter(school_id=1).values("school_year")
    if request.method == 'POST':
        headquarters_list = Headquarter.objects.all()                
        headquarter_selected = request.POST.getlist('headquarters')
        headquarter = headquarter_selected[0]
                       
        if headquarter == '-1':
            grades_list = Grade.objects.filter(grade_year = year)            
        else:
            grades_list = Grade.objects.filter(grade_year = year).filter(grade_headquarter = headquarter)
        
        return render_to_response('grades.html',{'grades':grades_list, 'headquarters':headquarters_list, 'headquarter_selected':int(headquarter)}, context_instance=RequestContext(request))
    else:
        grades_list = Grade.objects.filter(grade_year = year)
        headquarters_list = Headquarter.objects.all()
        
        try:
            message = request.session['message']
            del request.session['message']
            if message != '':
                return render_to_response('grades.html',{'grades':grades_list, 'message': message, 'headquarters':headquarters_list, 'headquarter_selected':'-1'}, context_instance=RequestContext(request))
        except KeyError:
            pass        
    return render_to_response('grades.html',{'grades':grades_list, 'headquarters':headquarters_list, 'headquarter_selected':'-1'}, context_instance=RequestContext(request))

@login_required(login_url='/')
def add_grade(request):
    warning = 0
    if request.method == 'POST':
        form = GradeForm(request.POST)        
        headquarter_selected = request.POST.getlist('grade_headquarter')
        headquarter = headquarter_selected[0]
        grades_select = request.POST.getlist('grade_name')
        grade = grades_select[0]        
       
        year = School.objects.filter(school_id=1).values("school_year")
        q = Grade.objects.filter(grade_year = year).filter(grade_name = grade).filter(grade_headquarter = headquarter)       
                
        if len(q)==0 and form.is_valid(): 
            grades = Grade()
            grades.grade_year = Year.objects.get(pk = year)
            grades.grade_headquarter = Headquarter.objects.get(pk = headquarter)
            grades.grade_name = str(grade)
            grades.save()            
            message = 'El grado ' + request.POST['grade_name'] + ' ha sido almacenado correctamente.'
            request.session['message'] = message            
            return HttpResponseRedirect('/grades') 
        else:
            warning = 2
            return render_to_response('grades.html', {'form':form, 'warning':warning}, context_instance = RequestContext(request))
    else:
        form = GradeForm()
    return render_to_response('grades.html', {'form':form}, context_instance = RequestContext(request))

@login_required(login_url='/')
def edit_grade(request, id_grade):
    try:
        grade = get_object_or_404(Grade, pk = id_grade)
    except Http404:
        return render_to_response('404.html', {'message': 'Lo sentimos grado no encontrado. Sonrie y dá click ', 'link': '/grades'}, context_instance = RequestContext(request))
    
    if request.method == 'POST':
        form = GradeForm(request.POST, instance = grade)
        headquarter_selected = request.POST.getlist('grade_headquarter')
        headquarter = headquarter_selected[0]
        grades_select = request.POST.getlist('grade_name')
        grades = grades_select[0]        
        year = School.objects.filter(school_id=1).values("school_year")
        q = Grade.objects.filter(grade_year = year).filter(grade_name = grades).filter(grade_headquarter = headquarter)
        
        if len(q)==0 and form.is_valid():
            form.save()
            message = 'El grado ' + grade.grade_name + ' ha sido editado correctamente.'
            request.session['message'] = message
            return HttpResponseRedirect('/grades')
        else:
            warning = 2
            return render_to_response('grades.html', {'form':form, 'warning':warning}, context_instance = RequestContext(request))
    else:
        form = GradeForm(instance = grade)
    return render_to_response('grades.html', {'form':form, 'edit':True}, context_instance = RequestContext(request))

@login_required(login_url='/')
def delete_grade(request, id_grade):
    try:
        grade = get_object_or_404(Grade, pk = id_grade)
    except Http404:
        return render_to_response('404.html', {'message': 'Lo sentimos grado no encontrado. Sonrie y dá click ', 'link': '/grades'}, context_instance = RequestContext(request))
        
    if request.method == 'POST':        
        try:
            grade.delete()
        except ProtectedError:
            return render_to_response('grades.html', {'grade':grade, 'delete':True, 'warning':'El grado ' + grade.grade_name + ' no puede ser eliminado, porqué está asociado a un curso'}, context_instance = RequestContext(request))
        
        message = 'El grado ' + grade.grade_name + ' ha sido eliminado correctamente.'
        request.session['message'] = message
        return HttpResponseRedirect('/grades')        
    return render_to_response('grades.html', {'grade':grade, 'delete':True}, context_instance = RequestContext(request))    
            

@login_required(login_url='/')
def grades_history(request):
    if request.method == 'POST':
        
        headquarters_list = Headquarter.objects.all()                
        headquarter_selected = request.POST.getlist('headquarters')
        headquarter = headquarter_selected[0]
        
        years_list = Year.objects.all()                
        year_selected = request.POST.getlist('years')
        year = year_selected[0]
        
        if headquarter == '-1':
            grades_history_list = Grade.objects.all()
        else:
            grades_history_list = Grade.objects.filter(grade_headquarter = headquarter) 
            
        if year != '-1':
            grades_history_list = grades_history_list.filter(grade_year = year)             
                    
        return render_to_response('grades_history.html',{'grades_history':grades_history_list, 'headquarters':headquarters_list, 'years':years_list, 'headquarter_selected':int(headquarter), 'year_selected':int(year)}, context_instance=RequestContext(request))
    else:
        grades_history_list = Grade.objects.all()
        headquarters_list = Headquarter.objects.all()
        years_list = Year.objects.all()
    return render_to_response('grades_history.html',{'grades_history':grades_history_list, 'headquarters':headquarters_list, 'years':years_list,  'headquarter_selected':'-1', 'year_selected':'-1'}, context_instance=RequestContext(request))

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
    headquarter = Headquarter.objects.get(pk = id_headquarter)
    if request.method == 'POST':
        form = HeadquarterForm(request.POST, instance = headquarter)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/headquarters')
    else:
        form = HeadquarterForm(instance = headquarter)
    return render_to_response('headquarters.html', {'form':form}, context_instance = RequestContext(request))

@login_required(login_url='/')
def delete_headquarter(request, id_headquarter):
    headquarter = Headquarter.objects.get(pk = id_headquarter) 
    if request.method == 'POST':
        headquarter.delete()
        return HttpResponseRedirect('/headquarters')
    return render_to_response('headquarters.html', {'headquarter':headquarter, 'delete':True}, context_instance = RequestContext(request))

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
def students(request):
    year = School.objects.filter(school_id = 1).values('school_year')
    
    if request.method == 'POST':
        return student_post(request, year)
    else:
        headquarters_list = Headquarter.objects.all()
        grades_list = Grade.objects.filter(grade_year = year)
        courses_list = Course.objects.filter(course_grade__in = grades_list)
        students_list = Student.objects.all()
        
        try:
            message = request.session['message']
            del request.session['message']
            if message != '':
                return render_to_response('students.html',{'students':students_list,'message': message,'headquarters': headquarters_list, 'grades':grades_list, 'courses':courses_list, 'state_selected':'-1', 
                                                   'headquarter_selected': '-1', 'grade_selected':'-1', 'course_selected':'-1'}, context_instance=RequestContext(request))
        except KeyError:
            pass
        
    return render_to_response('students.html',{'students':students_list,'headquarters': headquarters_list, 'grades':grades_list, 'courses':courses_list, 'state_selected':'-1', 
                                                   'headquarter_selected': '-1', 'grade_selected':'-1', 'course_selected':'-1'}, context_instance=RequestContext(request))    
    
@login_required(login_url='/')
def student_post(request, year):
    headquarters_list = Headquarter.objects.all()
    grades_list = []
    courses_list = []
    students_list = []
    
    state = request.POST.getlist('states')[0]
    headquarter = request.POST.getlist('headquarters')[0]
    grade = request.POST.getlist('grades')[0]
    course = request.POST.getlist('courses')[0]
    
    change = False
    
    if headquarter == '-1':
        grades_list = Grade.objects.filter(grade_year = year)
    else:
        grades_list = Grade.objects.filter(grade_year = year).filter(grade_headquarter = headquarter)
        change = True
    
    if grade == '-1':
        courses_list = Course.objects.filter(course_grade__in = grades_list)
    else:
        courses_list = Course.objects.filter(course_grade = grade)
        change = True
    
    if course == '-1':
        if change:
            students_list = Student.objects.filter(student_course__in = courses_list)
        else:
            students_list = Student.objects.all()         
    else:
        students_list = Student.objects.filter(student_course = course)  
    
    if state == '0':
        students_list = students_list.filter(student_matriculated = False)
    elif state == '1':
        students_list = students_list.filter(student_matriculated = True)
        
    return render_to_response('students.html',{'students':students_list, 'headquarters': headquarters_list, 'grades':grades_list, 'courses':courses_list, 'state_selected':state, 
                                           'headquarter_selected': int(headquarter), 'grade_selected':int(grade), 'course_selected': int(course)}, context_instance=RequestContext(request))

@login_required(login_url='/')
def add_student(request):
    if request.method == 'POST':
        form_student = StudentForm(request.POST)
        if form_student.is_valid():
            form_student.save()
            message = 'El estudiante ' + request.POST['student_first_name'] + ' ' + request.POST['student_last_name'] + ' ha sido almacenado correctamente.'
            request.session['message'] = message
            return HttpResponseRedirect('/students') 
    else:
        form_student = StudentForm()
    return render_to_response('students.html', {'form_student':form_student}, context_instance = RequestContext(request))

@login_required(login_url='/')
def details_student(request, id_student):
    try:
        student = get_object_or_404(Student, pk = id_student)
    except Http404:
        return render_to_response('404.html', {'message': 'Lo sentimos estudiante no encontrado. Sonrie y dá click ', 'link': '/students'}, context_instance = RequestContext(request))

    gender = ''
    if student.student_gender == 'F':
        gender = 'Femenino'
    else:
        gender = 'Masculino'
    if request.method == 'POST':
        return HttpResponseRedirect('/students')
    else:
        form_student = StudentForm(instance = student)
    return render_to_response('students.html', {'form_details':form_student, 'gender':gender}, context_instance = RequestContext(request))

@login_required(login_url='/')
def edit_student(request, id_student):
    try:
        student = get_object_or_404(Student, pk = id_student)
    except Http404:
        return render_to_response('404.html', {'message': 'Lo sentimos estudiante no encontrado. Sonrie y dá click ', 'link': '/students'}, context_instance = RequestContext(request))

    if request.method == 'POST':
        form_student = StudentForm(request.POST, instance = student)
        if form_student.is_valid():
            form_student.save()
            message = 'El estudiante ' + student.student_first_name + ' ' + student.student_last_name + ' ha sido editado correctamente.'
            request.session['message'] = message
            return HttpResponseRedirect('/students')
    else:
        form_student = StudentForm(instance = student)
    return render_to_response('students.html', {'form_student':form_student, 'edit': True}, context_instance = RequestContext(request))

@login_required(login_url='/')
def delete_student(request, id_student):
    try:
        student = get_object_or_404(Student, pk = id_student)
    except Http404:
        return render_to_response('404.html', {'message': 'Lo sentimos estudiante no encontrado. Sonrie y dá click ', 'link': '/students'}, context_instance = RequestContext(request))

    if request.method == 'POST':
        
        try:
            student.delete()
        except ProtectedError:
            return render_to_response('students.html', {'student_delete': student, 'warning': 'El estudiante ' + student.student_first_name + ' ' + student.student_last_name + ' no puede ser eliminado.'}, context_instance = RequestContext(request))
        
        message = 'El estudiante ' + student.student_first_name + ' ' + student.student_last_name + ' ha sido eliminado correctamente.'
        request.session['message'] = message
        return HttpResponseRedirect('/students')
    return render_to_response('students.html', {'student_delete': student}, context_instance = RequestContext(request))

@login_required(login_url='/')
def enrollment(request, id_student):
    year = School.objects.filter(school_id = 1).values('school_year')
    if request.method == 'POST':
        if request.POST.getlist('register_headquarters'):
            return update_enrollment(request, year, False)
        elif request.POST.getlist('register_courses'):
            try:
                student = get_object_or_404(Student, pk = id_student)
            except Http404:
                return render_to_response('404.html', {'message': 'Lo sentimos estudiante no encontrado. Sonrie y dá click ', 'link': '/students'}, context_instance = RequestContext(request))

            course = Course.objects.get(pk = int(request.POST.getlist('register_courses')[0]))
            student.student_course = course
            student.student_matriculated = 1
            student.save()
            if(course_history_exist(request, student)):
                message = 'El estudiante ' + student.student_first_name + ' ' + student.student_last_name + ' ha sido matriculado correctamente en' + ' ' + student.student_course.course_name + '.'
                request.session['message'] = message
                return HttpResponseRedirect('/students')
            else:
                course_history = Course_history()
                course_history.course_history_course = course
                course_history.course_history_student = student
                course_history.save()
                message = 'El estudiante ' + student.student_first_name + ' ' + student.student_last_name + ' ha sido matriculado correctamente en' + ' ' + student.student_course.course_name + '.'
                request.session['message'] = message
                return HttpResponseRedirect('/students')
        else:
            headquarters_list = Headquarter.objects.all()
            grades_list = Grade.objects.filter(grade_year = year)
            courses_list = Course.objects.filter(course_grade__in = grades_list)
            return render_to_response('students.html',{'register': True, 'warning': '*Este campo es obligatorio', 'headquarters': headquarters_list, 'grades':grades_list, 'courses':courses_list, 'headquarter_selected': '-1', 'grade_selected':'-1', 'course_selected':'-1'}, context_instance=RequestContext(request))
    else:
        headquarters_list = Headquarter.objects.all()
        grades_list = Grade.objects.filter(grade_year = year)
        courses_list = Course.objects.filter(course_grade__in = grades_list)
        
    return render_to_response('students.html',{'register': True, 'headquarters': headquarters_list, 'grades':grades_list, 'courses':courses_list, 'headquarter_selected': '-1', 'grade_selected':'-1', 'course_selected':'-1'}, context_instance=RequestContext(request))

@login_required(login_url='/')
def course_history_exist(request, student):
    course_history = Course_history.objects.filter(course_history_student = student).filter(course_history_course = student.student_course)
    
    if len(course_history) > 0:
        return True
    else:
        return False
    
@login_required(login_url='/')
def edit_enrollment(request, id_student):
    year = School.objects.filter(school_id = 1).values('school_year')
    try:
        student = get_object_or_404(Student, pk = id_student)
    except Http404:
        return render_to_response('404.html', {'message': 'Lo sentimos estudiante no encontrado. Sonrie y dá click ', 'link': '/students'}, context_instance = RequestContext(request))
    
    if request.method == 'POST':
        if request.POST.getlist('register_headquarters'):
            return update_enrollment(request, year, True)
        elif request.POST.getlist('register_courses'):
            if(student.student_course.course_id == request.POST.getlist('register_courses')[0]):
                message = 'El estudiante ' + student.student_first_name + ' ' + student.student_last_name + ' ha sido matriculado correctamente en' + ' ' + student.student_course.course_name + '.'
                request.session['message'] = message    
                return HttpResponseRedirect('/students')
            else:
                course = Course.objects.get(pk = int(request.POST.getlist('register_courses')[0]))
                if delete_course_history(request, student):
                    course_history = Course_history.objects.get(course_history_student = student, course_history_course = student.student_course)
                    student.student_course = course
                    student.save()           
                    if course_history_exist(request, student):
                        course_history.delete()
                    else:
                        course_history.course_history_course = course
                        course_history.course_history_student = student
                        course_history.save()
                else:
                    student.student_course = course
                    student.save()
                    if course_history_exist(request, student) == False:
                        course_history = Course_history()
                        course_history.course_history_course = course
                        course_history.course_history_student = student
                        course_history.save()
                message = 'El estudiante ' + student.student_first_name + ' ' + student.student_last_name + ' ha sido matriculado correctamente en' + ' ' + student.student_course.course_name + '.'
                request.session['message'] = message
                return HttpResponseRedirect('/students')
        else:
            headquarters_list = Headquarter.objects.all()
            grades_list = Grade.objects.filter(grade_year = year)
            courses_list = Course.objects.filter(course_grade__in = grades_list)
            return render_to_response('students.html',{'register': True, 'edit_enrollment': True, 'warning': '*Este campo es obligatorio','student_id': student.student_id, 'headquarters': headquarters_list, 'grades':grades_list, 'courses':courses_list, 'headquarter_selected': '-1', 'grade_selected':'-1', 'course_selected':student.student_course.course_id}, context_instance=RequestContext(request))
    else:
        headquarters_list = Headquarter.objects.all()
        grades_list = Grade.objects.filter(grade_year = year)
        courses_list = Course.objects.filter(course_grade__in = grades_list)
        
    return render_to_response('students.html',{'register': True, 'edit_enrollment': True, 'student_id': student.student_id, 'headquarters': headquarters_list, 'grades':grades_list, 'courses':courses_list, 'headquarter_selected': '-1', 'grade_selected':'-1', 'course_selected':student.student_course.course_id}, context_instance=RequestContext(request))

@login_required(login_url='/')
def update_enrollment(request, year, edit_enrollment):
    headquarters_list = Headquarter.objects.all()
        
    headquarter = request.POST.getlist('register_headquarters')[0]
    grade = request.POST.getlist('register_grades')[0]
    
    if headquarter == '-1':
        grades_list = Grade.objects.filter(grade_year = year)
    else:
        grades_list = Grade.objects.filter(grade_year = year).filter(grade_headquarter = headquarter)
    
    if grade == '-1':
        courses_list = Course.objects.filter(course_grade__in = grades_list)
    else:
        courses_list = Course.objects.filter(course_grade = grade)
    
    if edit_enrollment:
        return render_to_response('students.html',{'register': True, 'edit_enrollment': edit_enrollment, 'headquarters': headquarters_list, 'grades':grades_list, 'courses':courses_list, 'headquarter_selected': int(headquarter), 'grade_selected':int(grade)}, context_instance=RequestContext(request))
    else:
        return render_to_response('students.html',{'register': True, 'headquarters': headquarters_list, 'grades':grades_list, 'courses':courses_list, 'headquarter_selected': int(headquarter), 'grade_selected':int(grade)}, context_instance=RequestContext(request))

@login_required(login_url='/')
def cancel_enrollment(request, id_student):
    try:
        student = get_object_or_404(Student, pk = id_student)
    except Http404:
        return render_to_response('404.html', {'message': 'Lo sentimos estudiante no encontrado. Sonrie y dá click ', 'link': '/students'}, context_instance = RequestContext(request))
    
    if delete_course_history(request, student):
        course_history = Course_history.objects.get(course_history_student = student, course_history_course = student.student_course)
        course_history.delete()
    
    student.student_course = None
    student.student_matriculated = 0
    student.save()
    message = 'La matrícula del estudiante ' + student.student_first_name + ' ' + student.student_last_name + ' ha sido cancelada correctamente.'
    request.session['message'] = message
    return HttpResponseRedirect('/students')

@login_required(login_url='/')
def delete_course_history(request, student):
    course = Course.objects.filter(course_id = student.student_course.course_id)
    lists_allocation = Allocation.objects.filter(allocation_course = course)
    lists_score = Score.objects.filter(score_allocation__in = lists_allocation).filter(score_student = student)
    
    if len(lists_score) > 0:
        return False
    else:
        return True

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
    return render_to_response('subjects.html', {'form_new_subject':form}, context_instance = RequestContext(request))

@login_required(login_url='/')
def edit_subject(request, id_subject):
    subject = Subject.objects.get(pk = id_subject)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance = subject)
        if form.is_valid():
            form.save()
            subjects_list = Subject.objects.all()
            return render_to_response('subjects.html',{'subjects':subjects_list}, context_instance=RequestContext(request))
    else:
        form = SubjectForm(instance = subject)
    return render_to_response('subjects.html', {'form':form}, context_instance = RequestContext(request))

@login_required(login_url='/')
def delete_subject(request, id_subject):
    subject = Subject.objects.get(pk = id_subject)
    subject.delete()
    subjects_list = Subject.objects.all()
    return render_to_response('subjects.html',{'subjects':subjects_list}, context_instance=RequestContext(request))

@login_required(login_url='/')
def teachers(request):
    teachers_list = Teacher.objects.all()
    return render_to_response('teachers.html',{'teachers':teachers_list}, context_instance=RequestContext(request))

@login_required(login_url='/')
def teachers_history(request):
    teachers_list_history = Teacher.objects.all()
    return render_to_response('teachers_history.html',{'teachers':teachers_list_history}, context_instance=RequestContext(request))
                              
@login_required(login_url='/')
def add_teacher(request):
    teachers_list = Teacher.objects.all()
    if request.method == 'POST':
        if request.POST.get("Cancel"):
            print('cancel')
        else:
            form = TeacherForm(request.POST)
            if form.is_valid():
                form.save()
                teachers_list = Teacher.objects.all()
                return render_to_response('teachers.html',{'teachers':teachers_list}, context_instance=RequestContext(request)) 
    else:
        form = TeacherForm()
    return render_to_response('teachers.html', {'teachers':teachers_list,'form_teacher':form}, context_instance = RequestContext(request))

@login_required(login_url='/')
def details_teacher(request, id_teacher):
    teacher_view = Teacher.objects.get(pk = id_teacher)
    teachers_list = Teacher.objects.all()
    teacher_subjects = Subject.objects.raw("SELECT subject_id, subject_name FROM subject, allocation WHERE subject_id=allocation_subject_id AND allocation_teacher_id=%s", [id_teacher])
    teacher_grade = Course.objects.raw("SELECT course_id, course_name FROM course WHERE course_teacher_id=%s", [id_teacher])
    return render_to_response('teachers.html', {'teachers':teachers_list, 'teacher_view':teacher_view, 'teacher_subjects':teacher_subjects, 'teacher_grade':teacher_grade}, context_instance = RequestContext(request))

@login_required(login_url='/')
def edit_teacher(request, id_teacher):
    teacher = Teacher.objects.get(pk = id_teacher)
    teachers_list = Teacher.objects.all()
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance = teacher)
        if form.is_valid():
            form.save()
            teachers_new_list = Teacher.objects.all()
            return render_to_response('teachers.html',{'teachers':teachers_new_list}, context_instance=RequestContext(request))
    else:
        form = TeacherForm(instance = teacher)
    return render_to_response('teachers.html', {'teachers':teachers_list, 'form_teacher':form}, context_instance = RequestContext(request))

@login_required(login_url='/')
def delete_teacher(request, id_teacher):
    teacher_to_delete = Teacher.objects.get(pk = id_teacher)
    teachers_list = Teacher.objects.all()
    if request.method == 'POST':
        teacher = Teacher.objects.get(pk = id_teacher)
        teacher.delete()
        teachers_list = Teacher.objects.all()
        return render_to_response('teachers.html',{'teachers':teachers_list}, context_instance=RequestContext(request))
    return render_to_response('teachers.html', {'teachers':teachers_list,'teacher_to_delete':teacher_to_delete}, context_instance = RequestContext(request))

@login_required(login_url='/')
def reports(request):
    return render_to_response('reports.html',{'reports':reports}, context_instance=RequestContext(request))

@login_required(login_url='/')
def school(request):
    return render_to_response('school.html',{'school':school}, context_instance=RequestContext(request))

@login_required(login_url='/')
def edit_school(request, id_school):
    school = School.objects.get(pk = id_school)
    if request.method == 'POST':
        form = SchoolForm(request.POST, instance = school)
        if form.is_valid():
            form.save()
            schools_list = school.objects.all()
            return render_to_response('school.html',{'school':schools_list}, context_instance=RequestContext(request))
    else:
        form = SchoolForm(instance = school)
    return render_to_response('school.html', {'form':form}, context_instance = RequestContext(request))

@login_required(login_url='/')
def school_year(request):
    warning = 'Html en mantenimiento'
    return render_to_response('school.html', {'warning':warning}, context_instance = RequestContext(request))