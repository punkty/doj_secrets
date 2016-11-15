from django.shortcuts import render, HttpResponse, redirect
# from models whatever our tables are
  # Create your views here.
def index(request):
    return render(request, "secrets/index.html")