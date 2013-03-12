from django.forms.models import ModelForm

from WebSchool.models import Course
from WebSchool.models import Goal
from WebSchool.models import Grade
from WebSchool.models import School
from WebSchool.models import Score
from WebSchool.models import Student
from WebSchool.models import Subject
from WebSchool.models import Teacher

class CourseForm(ModelForm):
    class Meta:
        model =  Course
        
class GoalForm(ModelForm):
    class Meta:
        model =  Goal
        
class GradeForm(ModelForm):
    class Meta:
        model =  Grade
        
class HeadquarterForm(ModelForm):
    class Meta:
        model =  School

class ScoreForm(ModelForm):
    class Meta:
        model =  Score
        
class StudentForm(ModelForm):
    class Meta:
        model =  Student
        
class SubjectForm(ModelForm):
    class Meta:
        model =  Subject
        
class TeacherForm(ModelForm):
    class Meta:
        model =  Teacher