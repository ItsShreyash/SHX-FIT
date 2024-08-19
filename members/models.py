from django.db import models

# Create your models here.

class Members(models.Model):
    name = models.CharField(max_length=100 , null= False)
    Useremail = models.EmailField(max_length=200 , null= False)
    password = models.CharField(max_length=100 , null= False)
    Fitness_goal = models.CharField(max_length=100 ,default = "0")
    Fitness_level = models.CharField(max_length=100 ,default = "0")
    week_time = models.IntegerField( default = "0")
    
    def __str__(self):
        return self.name
    
class Video(models.Model):
    CATEGORY_CHOICES = [
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('powerlifting', 'Powerlifting'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    video_file = models.FileField(upload_to='videos/')