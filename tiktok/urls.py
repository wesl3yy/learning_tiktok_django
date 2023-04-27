from django.urls import path
from tiktok.campaign.views import CampaignView

urlpatterns = [
    path('campaign/create', CampaignView.as_view({'post': 'create'}), name='create_campaign')
]
