from django.db import models
from django.utils import timezone
from account.models import Account


# Create your models here.

class ViaAccount(models.Model):
    title = models.CharField(max_length=255)
    access_token = models.CharField(max_length=255)
    via_account_id = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    user_created = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.via_account_id
