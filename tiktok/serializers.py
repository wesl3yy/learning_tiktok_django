from rest_framework import serializers
from viaacount.models import ViaAccount
from tiktok.utils import create_campaign, convert_response
from tiktok.models import TiktokCampaign


class CreateCampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = TiktokCampaign
        exclude = ('campaign_id',)

    def create(self, validated_data):
        create_campaign_tiktok = create_campaign(validated_data)
        try:
            campaign = TiktokCampaign.objects.create(
                campaign_id=create_campaign_tiktok['data'].get('campaign_id'),
                campaign_name=validated_data['campaign_name'],
                objective_type=validated_data['objective_type'],
                advertiser_id=validated_data['advertiser_id'],
                budget_mode=validated_data['budget_mode'],
                budget=validated_data['budget'],
                operation_status=validated_data['operation_status'],
            )
        except:
            raise serializers.ValidationError(convert_response("Error", 400, {"error": "Create campaign failed"}))
        return campaign


class CreateAdGroupSerializer(serializers.ModelSerializer):
    pass
