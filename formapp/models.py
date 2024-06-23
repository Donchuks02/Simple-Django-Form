from django.db import models

# Create your models here.

class FormModel(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  phone_number = models.IntegerField()
  email = models.EmailField
  review_text = models.TextField()

  def __str__(self):
    return f"{self.first_name}{self.last_name}"
