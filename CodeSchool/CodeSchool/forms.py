#encoding:utf-8

from django.forms.models import ModelForm

from WebSchool.models import Course
from WebSchool.models import Goal
from WebSchool.models import Grade
from WebSchool.models import School
from WebSchool.models import Score
from WebSchool.models import Student
from WebSchool.models import Subject
from WebSchool.models import Teacher
from WebSchool.models import Headquarter
from django.forms.widgets import RadioSelect, TextInput, Select

import re
from django.core.exceptions import ValidationError

class CourseForm(ModelForm):
    class Meta:
        model =  Course
        
class GoalForm(ModelForm):
    class Meta:
        model =  Goal
        
class GradeForm(ModelForm):
    class Meta:
        model =  Grade
        GRADES = (
            ('Primero', 'Primero'),
            ('Segundo', 'Segundo'),
            ('Tercero', 'Tercero'),
            ('Cuarto', 'Cuarto'),
            ('Quinto', 'Quinto'),
            ('Sexto', 'Sexto'),
            ('Septimo', 'Septimo'),
            ('Octavo', 'Octavo'),
            ('Noveno', 'Noveno'),
            ('Decimo', 'Decimo'),
            ('Once', 'Once'),
            )
        widgets = {
            'grade_name': Select(choices=GRADES),
        }
        
class HeadquarterForm(ModelForm):
    class Meta:
        model =  Headquarter

class ScoreForm(ModelForm):
    class Meta:
        model =  Score
        
CHECK_ONLY_LETTERS = re.compile('[a-zA-Z]+$')
CHECK_ONLY_NUMBERS = re.compile('[0-9]+$')

class StudentForm(ModelForm):
    class Meta:
        model =  Student
        GENDERS = (('F', 'Femenino'),
                   ('M', 'Masculino'))
        widgets = {
            'student_gender': RadioSelect(choices=GENDERS),
            'student_date_of_birth': TextInput(attrs={'id':'student_date_of_birth'})
        }
        
    def clean_student_first_name(self):
        string = self.cleaned_data['student_first_name']
        if not CHECK_ONLY_LETTERS.match(string):
            raise ValidationError("Este campo solo acepta letras")
        return string
    
    def clean_student_last_name(self):
        string = self.cleaned_data['student_last_name']
        if not CHECK_ONLY_LETTERS.match(string):
            raise ValidationError("Este campo solo acepta letras")
        return string
    
    def clean_student_mobile_number(self):
        string = self.cleaned_data['student_mobile_number']
        if not CHECK_ONLY_NUMBERS.match(string):
            raise ValidationError("Este campo solo acepta números")
        return string
    
    def clean_student_document_id(self):
        string = self.cleaned_data['student_document_id']
        if not CHECK_ONLY_NUMBERS.match(string):
            raise ValidationError("Este campo solo acepta números")
        return string
        
class SubjectForm(ModelForm):
    class Meta:
        model =  Subject
        
class TeacherForm(ModelForm):
    class Meta:
        model =  Teacher

class SchoolForm(ModelForm):
    class Meta:
        model = School