from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=14)
    profile_pic = models.FileField(upload_to='profile_pic/')
    guardian = models.CharField(max_length=50)
    guardian_email = models.EmailField()
    guardian_phone_number = models.CharField(max_length=14)
    # house choices
    house_choices = [('africa','AFRICA'),('agarkhan','AGARKHAN'),('kakunguru','KAKUNGURU'),
                     ('luwangula','LUWANGULA')]
    house = models.CharField(max_length=10, choices=house_choices)

    # club choices
    club_choices = [('interact','INTERACT'),('aids','AIDS'),('rotery','ROTERY'),
                    ('nkobazambogo','NKOBAZAMBOGO')]
    club = models.CharField(max_length=20, choices=club_choices)

    # current class choices
    current_class_choices = [('f1','F1'),('f2','F2'),('f3','F3'),('f4','F4'),('f5','F5'),
                             ('f6','F6')]   
    current_class = models.CharField(max_length=10, choices=current_class_choices)

    # stream choices
    stream_choices = [('north','NORTH'),('east','EAST'),('west','WEST'),('south','SOUTH'),
                      ('sci-a','SCI-A'),('sci-b','SCI-B'),('arts','ARTS')]
    stream = models.CharField(max_length=10)

    # religion choices
    religion_choices = [('islam','ISLAM'),('christianity','CHRISTIANITY')]
    religion = models.CharField(max_length=20, choices=religion_choices)

    # gender choices
    gender_choices = [('male','MALE'),('female','FEMALE')]
    gender = models.CharField(max_length=10, choices=gender_choices)

    student_number = models.CharField(max_length=8)
    date_of_birth = models.DateField()
    date_joined = models.DateField()
    date_left = models.DateField(null=True,blank=True)

    combination = models.CharField(max_length=20)
    disabled = models.BooleanField()
    disabled_description = models.TextField()
    any_chronic_disease_condition = models.BooleanField()
    chronic_disease_condition_description = models.TextField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
