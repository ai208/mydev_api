from rest_framework import serializers
from health.models import Health

class HealthSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    updated = serializers.ReadOnlyField()
    class Meta:
        model = Health
        fields = ['id','weight','sleep_time','exercise_time','memo','created','updated']