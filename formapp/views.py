from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Form
from django.views import View

# Create your views here.

class FormView(View):
  def get(self, request):
    form = Form
    return render(request, "formapp/index.html", {"form": form})

  def post(self, request):
    form = Form(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect("/thank_you_page")


def thank_you_page(request):
  return render(request, "formapp/thankyou.html")