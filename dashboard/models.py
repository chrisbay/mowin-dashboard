from django.db import models
from django.contrib.auth.models import AbstractUser


class DashboardUser(AbstractUser):
    pass

class Dashboard(models.Model):
    pass