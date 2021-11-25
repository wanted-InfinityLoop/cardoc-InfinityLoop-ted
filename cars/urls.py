from django.urls import path
from cars.views import CarView

urlpatterns = [
    path("", CarView.as_view()),
    path("/users/tire", CarView.as_view()),
]
