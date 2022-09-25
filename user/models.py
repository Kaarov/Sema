from django.contrib.auth.models import AbstractUser
from django.db import models

ADMIN = 'admin'
TEACHER = 'teacher'
STUDENT = 'student'
USER = 'user'
USER_ROLE = ((ADMIN, 'Admin'), (TEACHER, 'Teacher'), (STUDENT, 'Student'), (USER, 'User'))


class User(AbstractUser):

    class Meta:
        db_table = 'my_user'
    role = models.CharField(max_length=20, choices=USER_ROLE)
    attempt = models.IntegerField(verbose_name="attempts", default=0)
    code = models.CharField(max_length=10, null=True, blank=True)
