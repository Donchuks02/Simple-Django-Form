from django.urls import path
from . import views

urlpatterns = [
  path("", views.FormView.as_view()),
  path("thank_you_page", views.thank_you_page)
]