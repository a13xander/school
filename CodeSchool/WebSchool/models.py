from django.db import models
#modelos

class Year(models.Model):
    year_id = models.AutoField(primary_key = True)
    year_value =  models.IntegerField(null = False)
    
    class Meta:
        db_table = "YEAR"
        
class School(models.Model):
    school_id = models.AutoField(primary_key = True)
    school_name =  models.CharField(max_length = 100, null = False)
    school_year = models.ForeignKey(Year)
    
    class Meta:
        db_table = "SCHOOL"

class Headquarter(models.Model):
    headquarter_id = models.AutoField(primary_key = True)
    headquarter_name =  models.CharField(max_length = 100, null = False)
    headquarter_address = models.CharField(max_length = 50, null = False)
    headquarter_phone = models.CharField(max_length = 10, null = False)
    headquarter_school = models.ForeignKey(School, blank = True, null = True)
    
    class Meta:
        db_table = "HEADQUARTER"
    
class Grade(models.Model):
    grade_id = models.AutoField(primary_key = True)
    grade_name =  models.CharField(max_length = 20, null = False)
    grade_year = models.ForeignKey(Year)
    grade_school = models.ForeignKey(School)
    
    class Meta:
        db_table = "GRADE"
        
class Subject(models.Model):
    subject_id = models.AutoField(primary_key = True)
    subject_name = models.CharField(max_length = 20, null = False)
    subject_hours = models.IntegerField(null = False)
    subject_grade = models.ForeignKey(Grade)
    
    class Meta:
        db_table = "SUBJECT"
        
class Period(models.Model):
    period_id = models.AutoField(primary_key = True)
    period_name = models.CharField(max_length = 10, null = False)
    period_start_date = models.DateField(null = False)
    period_end_date = models.DateField(null = False)
    
    class Meta:
        db_table = "PERIOD"
        
class Goal(models.Model):
    goal_id = models.AutoField(primary_key = True)
    goal_description = models.CharField(max_length = 1000, null = False)
    goal_subject = models.ForeignKey(Subject)
    goal_period = models.ForeignKey(Period)
    
    class Meta:
        db_table = "GOAL"
    
class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key = True)
    teacher_document_id = models.CharField(max_length = 12, null = False, unique = True)
    teacher_first_name = models.CharField(max_length = 50, null = False)
    teacher_last_name = models.CharField(max_length = 50, null = False)
    teacher_mobile_number = models.CharField(max_length = 10, null = False)
    teacher_address = models.CharField(max_length = 50, null = False)
    teacher_email = models.CharField(max_length = 50, null = False)
    teacher_hire_date = models.DateField(null = False)
    teacher_contracted = models.BooleanField(default = False)
    
    class Meta:
            db_table = "TEACHER"
            
class Course(models.Model):
    course_id = models.AutoField(primary_key = True)
    course_name = models.CharField(max_length = 20, null = False)
    course_grade = models.ForeignKey(Grade)
    course_teacher = models.ForeignKey(Teacher)
    
    class Meta:
        db_table = "COURSE"
            
class Allocation(models.Model):
    allocation_id = models.AutoField(primary_key = True)
    allocation_subject =  models.ForeignKey(Subject)
    allocation_course = models.ForeignKey(Course)
    allocation_teacher = models.ForeignKey(Teacher)
    
    class Meta:
        db_table = "ALLOCATION"
            
class Student(models.Model):
    student_id = models.AutoField(primary_key = True)
    student_code = models.IntegerField(null = False, unique = True)
    student_document_id = models.CharField(max_length = 12, null = False, unique = True)
    student_first_name = models.CharField(max_length = 50, null = False)
    student_last_name = models.CharField(max_length = 50, null = False)
    student_mobile_number = models.CharField(max_length = 10, null = False)
    student_address = models.CharField(max_length = 50, null = False)
    student_gender = models.CharField(max_length = 1, null = False)
    student_date_of_birth = models.DateField(null = False)
    student_matriculated = models.BooleanField(default = False)
    student_course = models.ForeignKey(Course, blank = True, null = True,)

    class Meta:
            db_table = "STUDENT"
            
class Score(models.Model):
    score_id = models.AutoField(primary_key = True)
    score_number = models.IntegerField(null = False)
    score_text = models.CharField(max_length = 15, null = False)
    score_student = models.ForeignKey(Student)
    score_period = models.ForeignKey(Period)
    score_allocation = models.ForeignKey(Allocation)
    
    class Meta:
            db_table = "SCORE"
            
class Course_history(models.Model):
    course_history_id = models.AutoField(primary_key = True)
    course_history_course = models.ForeignKey(Course)
    course_history_student = models.ForeignKey(Student)
    
    class Meta:
        db_table = "COURSE_HISTORY"

class Observation(models.Model):
    observation_id = models.AutoField(primary_key = True)
    observation_description = models.CharField(max_length = 1000, null = False)
    observation_period = models.ForeignKey(Period)
    observation_course_history = models.ForeignKey(Course_history)
    
    class Meta:
        db_table = "OBSERVATION"