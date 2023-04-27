from django.db import models
from django.utils import timezone

from account.models import Account



class TiktokCampaign(models.Model):
    ENABLED = 'ENABLE'
    DISABLED = 'DISABLE'
    OPERATION_STATUS_CHOICES = [
        (ENABLED, 'Enable'),
        (DISABLED, 'Disable')
    ]
    APP = 1
    LANDING_PAGE = 2
    BUDGET_MODE_TOTAL = 'BUDGET_MODE_TOTAL'
    BUDGET_MODE_DAY = 'BUDGET_MODE_DAY'
    BUDGET_MODE_INFINITE = 'BUDGET_MODE_INFINITE'
    BUDGET_MODE_CHOICES = [
        (BUDGET_MODE_DAY, 'Budget mode day'),
        (BUDGET_MODE_TOTAL, 'Budget mode total'),
        (BUDGET_MODE_INFINITE, 'Budget mode infinite')
    ]
    WEB_CONVERSIONS = 'WEB_CONVERSIONS'
    REACH = 'REACH'
    TRAFFIC = 'TRAFFIC'
    VIDEO_VIEWS = 'VIDEO_VIEWS'
    PRODUCT_SALES = 'PRODUCT_SALES'
    ENGAGEMENT = 'ENGAGEMENT'
    LEAD_GENERATION = 'LEAD_GENERATION'
    RF_REACH = 'RF_REACH'
    obj_type_choices = [
        (WEB_CONVERSIONS, 'Web conversions'),
        (REACH, 'Reach'),
        (TRAFFIC, 'Traffic'),
        (VIDEO_VIEWS, 'Video views'),
        (PRODUCT_SALES, 'Product sales'),
        (ENGAGEMENT, 'Engagement'),
        (LEAD_GENERATION, 'Lead generation'),
        (RF_REACH, 'RF Reach')
    ]
    campaign_id = models.CharField(max_length=255, unique=True)
    campaign_name = models.CharField(max_length=255, unique=True)
    advertiser_id = models.CharField(max_length=255)
    budget = models.FloatField(max_length=100, blank=True, null=True, default=0)
    budget_mode = models.CharField(choices=BUDGET_MODE_CHOICES, max_length=100)
    operation_status = models.CharField(choices=OPERATION_STATUS_CHOICES, default=ENABLED)
    objective_type = models.CharField(choices=obj_type_choices, max_length=100)
    created_time = models.DateTimeField(auto_now_add=timezone.now())
    updated_at = models.DateTimeField(auto_now_add=timezone.now())

    class Meta:
        db_table = 'campaign_tiktok'
        managed = True
