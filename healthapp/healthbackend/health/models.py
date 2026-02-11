from django.db import models
from django.conf import settings
# Create your models here.
class Health(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    weight = models.IntegerField(blank=False,null=False)
    sleep_time = models.IntegerField(blank=False,null=False)
    exercise_time = models.IntegerField(blank=False,null=False)
    memo = models.TextField(blank=True,null= True,max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.user}-{self.created}'
    class Meta:
        ordering = ['-created']