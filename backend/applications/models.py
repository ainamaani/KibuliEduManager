from django.db import models

# Create your models here.
class Application(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=6)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    current_class = models.CharField(max_length=20)
    school = models.CharField(max_length=50)
    school_location = models.CharField(max_length=30)
    school_phone_number = models.CharField(max_length=20)
    change_reason = models.TextField()
    date_of_application = models.DateField()
    class_applied_for = models.CharField(max_length=20)
    recommendation_letter = models.FileField()
    passport_photo = models.FileField()
    guardian_name = models.CharField(max_length=30)
    guardian_phone_number = models.CharField(max_length=20)
    guardian_email = models.EmailField()
    relationship_with_guardian = models.CharField(max_length=20)
    results_document = models.FileField()
    application_status = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
