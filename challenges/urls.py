from django.urls import path
from . import views


urlpatterns = [
    path("" , views.index),
    path("<int:month>" , views.monthly_challenge_by_number),
    path("<month>" , views.monthly_challenge, name = "monthly-challenges")
]
