from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_agent = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=50)
    location = models.CharField(max_length = 100)
    profile_picture = models.ImageField(upload_to='profile_img')

    class Meta:
        db_table = 'agent'
    
    def __str__(self):
        return str(self.user.first_name) + " " + str(self.user.last_name) + " from " + str(self.company)
    

class Client(models.Model):
    Stages = (
        ('Stage One', 'Just Looking!'),
        ('Stage Two', 'Ready To Move.'),
        ('Stage Three', 'Exploring Financing Options.'),
        ('Stage Four', 'Just Found Our Dream Home!'),
    )

    Scores = (
        ('< 700', '<700'),
        ('700 - 739', '700 - 739'),
        ('740 - 779', '740 - 779'),
        ('780 +', '780 +'),
    )

    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    buying_stage = models.CharField(max_length=100, choices=Stages)
    city_name = models.CharField(max_length = 100)    
    low_price = models.PositiveIntegerField(null=True)
    high_price = models.PositiveIntegerField(null=True)
    household_income = models.PositiveIntegerField(null=True)
    cash_inv = models.PositiveIntegerField(null=True)
    credit_score = models.CharField(max_length=50, choices=Scores, null=True)


    class Meta:
        db_table = "client"