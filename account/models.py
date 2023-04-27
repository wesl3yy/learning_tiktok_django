from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from account.tests import CustomUserManager


# Create your models here.

class Address(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    lat = models.FloatField(null=True, blank=True, default=None)
    long = models.FloatField(null=True, blank=True, default=None)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class AccountType(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=255, blank=True, null=True, default=None)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class WorkSpace(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True, default=None)
    target = models.CharField(max_length=255, null=True, blank=True, default=None)
    status = models.BooleanField(default=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class AccountRelative(models.Model):
    title = models.CharField(max_length=255)
    access_token = models.CharField(max_length=300, blank=True, null=True, default=None)
    code = models.IntegerField(choices=((1, 'Facebook'), (2, 'Instagram')), default=1)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Account(AbstractUser):
    email = models.EmailField(max_length=50, unique=True)
    key_account = models.CharField(max_length=255, default=None, blank=True, null=True)
    full_name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True, default=None)
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True)
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    account_type = models.OneToOneField(AccountType, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    account_relative = models.ManyToManyField(AccountRelative, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Role(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=255, blank=True, null=True, default=None)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class AccountWorkSpace(models.Model):
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    workspace = models.ForeignKey(WorkSpace, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.account.email + ' - ' + self.workspace.title
