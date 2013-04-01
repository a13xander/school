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
    if request.method == 'POST':
        headquarters_list = Headquarter.objects.all()
                
        headquarter_selected = request.POST.getlist('headquarters')
        headquarter = headquarter_selected[0]
        
        if headquarter == '-1':
            grades_list = Grade.objects.all()
        else:
            grades_list = Grade.objects.filter(grade_headquarter = headquarter)        
        
        return render_to_response('grades.html',{'grades':grades_list, 'headquarters':headquarters_list, 'headquarter_selected':int(headquarter)}, context_instance=RequestContext(request))
    else:
        grades_list = Grade.objects.all()
        headquarters_list = Headquarter.objects.all()
    return render_to_response('grades.html',{'grades':grades_list, 'headquarters':headquarters_list, 'headquarter_selected':'-1'}, context_instance=RequestContext(request))

@login_required(login_url='/')
def add_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)        
        headquarter_selected = request.POST.getlist('grade_headquarter')
        headquarter = headquarter_selected[0]
        grades_select = request.POST.getlist('grade_name')
        grade = grades_select[0]        
        sc = School.objects.get(pk = 1)
        q = Grade.objects.filter(grade_year = sc.school_year).filter(grade_name = grade).filter(grade_headquarter = headquarter)
        print(q)
        if len(q)==0 and form.is_valid(): 
            form.save()
            return HttpResponseRedirect('/grades') 
        else:
            return render_to_response('grades.html', {'form':form, 'warning':'sffsdfsd'}, context_instance = RequestContext(request))
    else:
        form = GradeForm()
    return render_to_response('grades.html', {'form':form}, context_instance = RequestContext(request))

@login_required(login_url='/')
def edit_grade(request, id_grade):
    grade = Grade.objects.get(pk = id_grade)
    if request.method == 'POST':
        form = GradeForm(request.POST, instance = grade)
        headquarter_selected = request.POST.getlist('grade_headquarter')
        headquarter = headquarter_selected[0]
        grades_select = request.POST.getlist('grade_name')
        grade = grades_select[0]        
        sc = School.objects.get(pk = 1)
        q = Grade.objects.filter(grade_year = sc.school_year).filter(grade_name = grade).filter(grade_headquarter = headquarter)
        print(q)
        if len(q)==0 and form.is_valid():
            form.save()
            return HttpResponseRedirect('/grades')
    else:
        form = GradeForm(instance = grade)
    return render_to_response('grades.html', {'form':form}, context_instance = RequestContext(request))

@login_required(login_url='/')
def delete_grade(request, id_grade):
    grade = Grade.objects.get(pk = id_grade)
    if request.method == 'POST':
        grade.delete()
        return HttpResponseRedirect('/grades')
    return render_to_response('grades.html', {'grade':grade, 'delete':True}, context_instance = RequestContext(request))

@login_required(login_url='/')
def grades_history(request):
    return render_to_response('grades_history.html',{'grades_history':grades_history}, context_instance=RequestContext(request))

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
    headquarter.delete()
    return HttpResponseRedirect('/headquarters')

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
    if request.method == 'POST':
        grades_list = Grade.objects.all()
        courses_list = []
        query = ''
        first = True
        
        states = request.POST.getlist('states')
        state = states[0]
        grades_select = request.POST.getlist('grades')
        grade = grades_select[0]
        courses_select = request.POST.getlist('courses')
        course = courses_select[0]
        
        if grade == '-1':
            courses_list = Course.objects.all()
            students_list = Student.objects.all()
            query = 'select student_id, student_code, student_first_name, student_last_name, student_course_id from student'
        else:
            courses_list = Course.objects.filter(course_grade = grade)
            first = False
            query = 'select student_id, student_code, student_first_name, student_last_name, student_course_id from student, course, grade where student_course_id = course_id and course_grade_id = grade_id and grade_id = ' + grade

        if course != '-1':
            if first:
                query += ' where student_course_id = ' + course
                first = False
            else:
                query += ' and student_course_id = ' + course            
                
        if state == '0':
            if first:
                query += ' where student_matriculated = 0'
            else:
                query += ' and student_matriculated = 0'
        elif state == '1':
            if first:
                query += ' where student_matriculated = 1'
            else:
                query += ' and student_matriculated = 1'
        
        students_list = Student.objects.raw(query)
               
        return render_to_response('students.html',{'students':students_list, 'grades':grades_list, 'courses':courses_list, 'state_selected':state, 
                                               'grade_selected':int(grade), 'course_selected': int(course)}, context_instance=RequestContext(request))
    else:
        grades_list = Grade.objects.all()
        courses_list = Course.objects.all()
        students_list = Student.objects.all()
    return render_to_response('students.html',{'students':students_list, 'grades':grades_list, 'courses':courses_list, 'state_selected':'-1', 
                                               'grade_selected':'-1', 'course_selected':'-1'}, context_instance=RequestContext(request))

@login_required(login_url='/')
def add_student(request):
    if request.method == 'POST':
        form_student = StudentForm(request.POST)
        if form_student.is_valid():
            form_student.save()
            return HttpResponseRedirect('/students') 
    else:
        form_student = StudentForm()
    return render_to_response('students.html', {'form':form_student}, context_instance = RequestContext(request))

@login_required(login_url='/')
def consult_student(request, id_student):
    student = Student.objects.get(pk = id_student)
    gender = ''
    if student.student_gender == 'F':
        gender = 'Femenino'
    else:
        gender = 'Masculino'
    if request.method == 'POST':
        return HttpResponseRedirect('/students')
    else:
        form_student = StudentForm(instance = student)
    return render_to_response('students.html', {'form':form_student, 'consult':True, 'gender':gender}, context_instance = RequestContext(request))

@login_required(login_url='/')
def edit_student(request, id_student):
    student = Student.objects.get(pk = id_student)
    if request.method == 'POST':
        form_student = StudentForm(request.POST, instance = student)
        if form_student.is_valid():
            form_student.save()
            return HttpResponseRedirect('/students')
    else:
        form_student = StudentForm(instance = student)
    return render_to_response('students.html', {'form':form_student, 'edit':True}, context_instance = RequestContext(request))

@login_required(login_url='/')
def delete_student(request, id_student):
    student = Student.objects.get(pk = id_student)
    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect('/students')
    return render_to_response('students.html', {'student':student, 'delete':True}, context_instance = RequestContext(request))

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