from django import forms
from .models import FormModel


class Form(forms.ModelForm):
  class Meta:
    model = FormModel
    fields = "__all__"
    labels = {
      "first_name": "First Name",
      "last_name": "Last Name ",
      "phone_number": "Phone Number",
      "email": "Email Address",
      "review_text": "Your Message",
 }
    error_messages = {
      "first_name":{
        "required": "Your name must not be empty !",
        "max_lenght": "Please enter a shorter name !"
      }
    }
