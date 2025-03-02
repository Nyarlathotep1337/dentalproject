from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Location(models.Model):
    city = models.CharField(max_length=100)
    address = models.TextField()
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.city

class Testimonial(models.Model):
    patient_name = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.patient_name} ({self.rating}/5)"

class Inquiry(models.Model):
    TREATMENT_CHOICES = [
        ('dental_implants', 'Dental Implants'),
        ('veneers', 'Veneers'),
        ('braces', 'Braces'),
        ('teeth_whitening', 'Teeth Whitening'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    treatment_type = models.CharField(max_length=50, choices=TREATMENT_CHOICES, default='other')
    preferred_location = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry from {self.name} ({self.treatment_type})"
