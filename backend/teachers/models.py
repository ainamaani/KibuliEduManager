from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Teacher(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=14, 
                 validators=[MinLengthValidator(limit_value=10, message='Phone number must not be less than 10 digits')])
    gender = models.CharField(max_length=8)
    address = models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to='teachers_pics/',blank=True,null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    qualifications = models.TextField(null=True, blank=True)
    subjects_taught = models.ManyToManyField('subjects.Subject', blank=True)
    classes_taught = models.CharField(max_length=100)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'


