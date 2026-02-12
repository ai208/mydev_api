from django.urls import path
from. import views

urlpatterns = [
    path('healths/',views.HealthList.as_view()),
]
