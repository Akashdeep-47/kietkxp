
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from users.models import UserProfile
from django.urls import reverse
from django import forms
from django.core.validators import RegexValidator

CATEGORIES=[
    ('BOOKS','BOOKS'),
    ('LAB ACCESSORIES','LAB ACCESSORIES'),
    ('ELECTRONICS','ELECTRONICS'),
    ('OTHERS','OTHERS')
]

class Post(models.Model):
    Product_name= models.CharField(max_length=30)
    desc= models.TextField()
    price= models.IntegerField()
    category= models.CharField(max_length=20,choices=CATEGORIES,default="")
    date_posted= models.DateTimeField(default=timezone.now)
    posted_by=models.ForeignKey(User, on_delete=models.CASCADE)
    Phone_number = models.CharField(max_length=10,
                                     validators=[RegexValidator(regex='^[6789][0-9]{9}$',
                                     message='Invalid mobile number entered',code='Invalid'),])
    image = models.ImageField(default='avatar.jpg')

    Image= models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return self.Product_name

    def get_absolute_url(self):
        return reverse('blog-home')



