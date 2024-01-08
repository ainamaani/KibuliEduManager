from django.db import models

# Create your models here.
class Application(models.Model):
    # Personal Information
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=6, choices=[('male', 'Male'), ('female', 'Female')])
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=50)

    # School Information
    current_class = models.CharField(max_length=20)
    school = models.CharField(max_length=50)
    school_location = models.CharField(max_length=30)
    school_phone_number = models.CharField(max_length=20)
    change_reason = models.TextField()
    date_of_application = models.DateTimeField(auto_now_add=True)
    class_applied_for = models.CharField(max_length=20)

    # Documents
    recommendation_letter = models.FileField(upload_to='recommendation_letters/', null=True, blank=True)
    passport_photo = models.FileField(upload_to='passport_photos/')
    results_document = models.FileField(upload_to='results_documents/')

    # Guardian Information
    guardian_name = models.CharField(max_length=30)
    guardian_phone_number = models.CharField(max_length=20)
    guardian_email = models.EmailField(blank=True, null=True)
    relationship_with_guardian = models.CharField(max_length=20)

    # Application Status
    application_status_choices = [('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')]
    application_status = models.CharField(max_length=30, choices=application_status_choices, blank=True, default='pending')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'
    
