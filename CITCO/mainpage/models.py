from django.db import models

# Create your models here.
class candidatemodel(models.Model):
    gender_choice=[
        ("Male","Male"),
        ("Female","Female"),
        ("Others","Others"),
    ]
    Qualification_choice=[
        ("B-tech","B-tech"),
        ("B.com","B.com"),
        ("MCA","MCA"),
        ("MBA","MBA"),
        ("Others","Others"),
    ]
    Name=models.CharField(max_length=30)
    Email=models.EmailField(unique=True)
    Password=models.CharField(max_length=30)
    Gender=models.CharField(max_length=30,choices=gender_choice)
    Qualification=models.CharField(max_length=30,choices=Qualification_choice)
    Upload_Image=models.ImageField(upload_to='Images/')
    Upload_Resume=models.FileField(upload_to="resume/",max_length=5000000)

    def __str__(self):
        return self.Name
