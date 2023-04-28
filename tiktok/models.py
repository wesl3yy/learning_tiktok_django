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


class TiktokAdGroup(models.Model):
    ENABLED = 'ENABLE'
    DISABLED = 'DISABLE'
    OPERATION_STATUS_CHOICES = [
        (ENABLED, 'Enable'),
        (DISABLED, 'Disable')
    ]
    UNSET = 'UNSET'
    VIDEO = 'VIDEO'
    LIVE = 'LIVE'
    CATALOG_LISTING_ADS = 'CATALOG_LISTING_ADS'
    SHOPPING_ADS_TYPE_CHOICES = [
        (UNSET, 'Unset'),
        (VIDEO, 'Video'),
        (LIVE, 'Live'),
        (CATALOG_LISTING_ADS, 'Catalog listing ads')
    ]
    LAB_1 = 'LAB_1'
    LAB_2 = 'LAB_2'
    LAB_3 = 'LAB_3'
    OFF = 'OFF'
    SHOPPING_ADS_RETARGETING_TYPE_CHOICES = [
        (LAB_1, 'Retargeting audiences who viewed products or added products to cart but didnt purchase products'),
        (LAB_2, 'Retargeting audiences who added products to cart but didnt purchase products. '),
        (LAB_3, 'Retargeting audiences using custom combination.'),
        (OFF, 'Off')
    ]
    BUDGET_MODE_TOTAL = 'BUDGET_MODE_TOTAL'
    BUDGET_MODE_DAY = 'BUDGET_MODE_DAY'
    BUDGET_MODE_INFINITE = 'BUDGET_MODE_INFINITE'
    BUDGET_MODE_CHOICES = [
        (BUDGET_MODE_DAY, 'Budget mode day'),
        (BUDGET_MODE_TOTAL, 'Budget mode total'),
        (BUDGET_MODE_INFINITE, 'Budget mode infinite')
    ]
    SCHEDULE_START_END = 'SCHEDULE_START_END'
    SCHEDULE_FROM_NOW = 'SCHEDULE_FROM_NOW'
    SCHEDULE_TYPE_CHOICES = [
        (SCHEDULE_START_END, 'Schedule start time mode'),
        (SCHEDULE_FROM_NOW, 'Schedule start now')
    ]
    PACING_MODE_SMOOTH = 'PACING_MODE_SMOOTH'
    PACING_MODE_FAST = 'PACING_MODE_FAST'
    PACING_MODE_CHOICES = [
        (PACING_MODE_FAST, 'Pacing mode fast'),
        (PACING_MODE_SMOOTH, 'Pacing mode smooth')
    ]
    TRANS_TYPE_TRANSFER = 'TRANS_TYPE_TRANSFER'
    TRANS_TYPE_TAX = 'TRANS_TYPE_TAX'
    TRANS_TYPE_COST = 'TRANS_TYPE_COST'
    BILLING_CHOICES = [
        (TRANS_TYPE_TRANSFER, 'Transfer'),
        (TRANS_TYPE_TAX, 'Consumption'),
        (TRANS_TYPE_COST, 'Tax')
    ]
    advertiser_id = models.CharField(max_length=255)
    campaign_id = models.ForeignKey(TiktokCampaign, on_delete=models.DO_NOTHING, null=False, related_name='campaign')
    adgroup_id = models.CharField(max_length=255)
    operation_status = models.CharField(choices=OPERATION_STATUS_CHOICES, max_length=100)
    adgroup_name = models.CharField(max_length=255)
    placement_type = models.CharField(max_length=255)
    comment_disable = models.BooleanField()
    promotion_target_type = models.CharField(max_length=255)
    shopping_ads_type = models.CharField(choices=SHOPPING_ADS_TYPE_CHOICES, max_length=100)
    shopping_ads_retargeting_type = models.CharField(max_length=255, choices=SHOPPING_ADS_RETARGETING_TYPE_CHOICES)
    budget = models.FloatField(max_length=100, blank=True, null=True, default=0)
    budget_mode = models.CharField(choices=BUDGET_MODE_CHOICES, max_length=100)
    schedule_type = models.CharField(choices=SCHEDULE_TYPE_CHOICES, max_length=100)
    schedule_start_time = models.DateTimeField()
    schedule_end_time = models.DateTimeField()
    pacing = models.CharField(choices=PACING_MODE_CHOICES, max_length=100)
    billing_event = models.CharField(choices=BILLING_CHOICES, max_length=100)

    def __str__(self):
        return self.campaign_id.campaign_name

    class Meta:
        db_table = 'tiktok_adgroup'
        managed = True
