from rest_framework import generics,permissions
from.serializers import HealthSerializer
from health.models import Health
from django.db import IntegrityError
from django.contrib.auth import get_user_model
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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

@csrf_exempt
def signup(request):
    if request.method =='POST':
        try:
            data = JSONParser().parse(request)
            User = get_user_model()
            user = User.objects.create_user(
                username=data['username'],
                password=data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)},status=201)
        except IntegrityError:
            return JsonResponse(
                {'error':'username taken. choose another username'},status = 400)


