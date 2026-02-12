from rest_framework import generics,permissions
from.serializers import HealthSerializer
from health.models import Health
# Create your views here.
class HealthListCreate(generics.ListCreateAPIView):
    serializer_class = HealthSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Health.objects.filter(user=user).order_by('created')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class HealthRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HealthSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Health.objects.filter(user=user)
