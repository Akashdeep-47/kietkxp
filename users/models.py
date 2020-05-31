from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.core.validators import RegexValidator

class signup(models.Model):
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=5)
    year = models.IntegerField()
    phone = PhoneField(blank=True, help_text='Contact phone number')



YEAR=[
    ('I','FIRST'),
    ('II','SECOND'),
    ('III','THIRD'),
    ('IV','FOURTH')
]

BRANCH=[
    ('CSE','CSE'),
    ('IT','IT'),
    ('CSI','CSI'),
    ('CO','CO'),
    ('CE','CE'),
    ('ECE','ECE'),
    ('EN','EN'),
    ('ME','ME'),
    ('OTHERS','OTHERS'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    branch = models.CharField(max_length=6,choices=BRANCH,default="")
    mobile_number = models.CharField(max_length=10,
                                     validators=[RegexValidator(regex='^[6789][0-9]{9}$',
                                     message='Invalid mobile number entered',code='Invalid')])
    image = models.ImageField(default='avatar.jpg')

    def __str__(self):
        return self.user.username


