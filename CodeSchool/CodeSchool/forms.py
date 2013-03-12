from django.forms.models import ModelForm
from WebSchool.models import Student

class StudentForm(ModelForm):
    class Meta:
        model =  Student