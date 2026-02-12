from django.urls import path
from. import views

urlpatterns = [
    path('healths/',views.HealthListCreate.as_view()),
    path('healths/<int:pk>',views.HealthRetrieveUpdateDestroy.as_view()),
]
