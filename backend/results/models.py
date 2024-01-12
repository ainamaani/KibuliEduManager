from django.db import models
from students.models import Student
from teachers.models import Teacher
from subjects.models import Subject
from django.core.validators import MaxValueValidator

# Create your models here.
class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    # term choices
    term_choices = [('1','1'),('2','2'),('3','3')]
    term = models.CharField(max_length=20, choices=term_choices)
    uploaded_by = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    mark = models.PositiveSmallIntegerField(validators=[MaxValueValidator(limit_value=100)])
    # grade choices
    grade_choices = [('a','A'),('b','B'),('c','C'),('d','D'),('e','E'),('f','F'),
                     ('d1','D1'),('d2','D2'),('c3','C3'),('c4','C4'),('c5','C6'),
                     ('p7','P7'),('p8','P8'),('f9','F9')
                     ]
    grade = models.CharField(max_length=2, choices=grade_choices)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    # student class choices
    student_class_choices = [('f1','F1'),('f2','F2'),('f3','F3'),('f4','F4'),('f5','F5'),
                             ('f6','F6')]
    student_class = models.CharField(max_length=20, choices=student_class_choices)


    def __str__(self) -> str:
        return self.student_class
    
    class Meta:
        verbose_name = 'Result'
        verbose_name_plural = 'Results'


    
