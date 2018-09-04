from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + ", is active: " + self.is_active

class UserProfile(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role,on_delete=models.CASCADE)
    summary = models.CharField(max_length=1000)
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{0} {1}".format(self.user_id.first_name, self.user_id.last_name)