from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + ", " + self.description

class UserProfile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='avatar.jpg', upload_to='profile_pics')
    role_id = models.ForeignKey(Role,on_delete=models.CASCADE)
    summary = models.CharField(max_length=1000)
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user_id.username} Profile'