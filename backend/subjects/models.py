from django.db import models


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=30)
    description = models.TextField()
    taught_by = models.ForeignKey('teachers.Teacher', on_delete=models.SET_NULL, null=True)
    # class_level_choices
    class_level_choices = [('f1','F1'),('f2','F2'),('f3','F3'),('f4','F4'),('f5','F5'),
                             ('f6','F6')]
    class_level = models.CharField(max_length=20, choices=class_level_choices)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

