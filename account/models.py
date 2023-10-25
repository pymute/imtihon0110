from django.db import models
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    CHOICE_ROLES = (
        (1, 'reader'),
        (2, 'write'),
        (3, 'admin')
    )
    role = models.PositiveSmallIntegerField(default=1, choices=CHOICE_ROLES)
    phone = models.CharField(default='', max_length=10, null=True)
