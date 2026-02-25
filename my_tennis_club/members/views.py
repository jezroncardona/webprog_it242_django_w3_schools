from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def members(request):
  return HttpResponse("<h2>Hello WEBPROG IT242 world! From Jez")