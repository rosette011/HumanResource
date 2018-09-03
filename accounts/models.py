from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + ", is active: " + self.is_active

class UserExtension(models.Model,User,Role):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role,on_delete=models.CASCADE)
    user_photo = models.FileField()
    user_file = models.FileField()
    create_date = models.DateTimeField(auto_now_add=True, blank=True)
    is_active = models.BooleanField(default=True)