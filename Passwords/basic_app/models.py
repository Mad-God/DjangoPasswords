from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfileInfo(models.Model):
    # create a relation to the 'User' in-built class
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user = User.objects.create()

    # additional features
    portfolio = models.URLField(blank = True)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)

    def __str__(self):
        return self.user.username



