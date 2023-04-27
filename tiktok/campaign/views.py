from rest_framework.views import Response, APIView
from rest_framework.permissions import IsAuthenticated
from tiktok.serializers import CreateCampaignSerializer, CreateAdGroupSerializer
from rest_framework import viewsets, generics


class CampaignView(viewsets.ViewSetMixin, generics.GenericAPIView, APIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = CreateCampaignSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        campaign = serializer.save()
        return Response(CreateCampaignSerializer(campaign, context=self.get_serializer_context()).data)


class AdGroupView(APIView, viewsets.ViewSetMixin, generics.GenericAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = CreateAdGroupSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        adgroup = serializer.save()
        return Response(CreateAdGroupSerializer(adgroup, context=self.get_serializer_context()).data)
