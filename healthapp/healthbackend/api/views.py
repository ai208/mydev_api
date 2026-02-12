from rest_framework import generics
from.serializers import HealthSerializer
from health.models import Health
# Create your views here.
class HealthList(generics.ListAPIView):
    serializer_class = HealthSerializer
    def get_queryset(self):
        user = self.request.user
        return Health.objects.filter(user=user).order_by('created')
