from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from django_better_admin_arrayfield.models.fields import ArrayField

from .managers import UserManager


class Profile(AbstractBaseUser, PermissionsMixin):
    """ Model for user profile """
    username = models.CharField(verbose_name='Username', max_length=255,
                                unique=True)

    first_name = models.CharField(verbose_name='First name', max_length=100,
                                  blank=True, default='')
    last_name = models.CharField(verbose_name='Last name', max_length=100,
                                 blank=True, default='')
    birthday = models.DateField(verbose_name="Birthday",
                                blank=True, null=True)
    biography = models.TextField(verbose_name="Biography",
                                 blank=True, null=True)
    contacts = ArrayField(verbose_name="Contacts", null=True, blank=True,
                          base_field=models.CharField(max_length=100,
                                                      default=''))

    date_joined = models.DateTimeField(verbose_name='Date joined',
                                       auto_now_add=True)
    terms = models.BooleanField(verbose_name='Terms', default=True)
    is_staff = models.BooleanField('Staff status', default=False)
    is_active = models.BooleanField(verbose_name='Active', default=True)

    ip = models.CharField(verbose_name='IP', max_length=15,
                          blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

    class Meta:
        ordering = ['username']


class Note(models.Model):
    """ Model for records for users create|update|delete operations """
    username = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    signal_type = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.username} -- {self.signal_type}"

    class Meta:
        ordering = ['-date']
