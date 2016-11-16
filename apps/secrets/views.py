from django.shortcuts import render, HttpResponse, redirect
from models import User, Secret
from django.contrib import messages
# from models whatever our tables are
  # Create your views here.

def session_check(request):
  if 'user' in request.session:
      return True
  else:
      return False

def print_errors(request, error_list):
    for error in error_list:
        messages.add_message(request, messages.INFO, error)

def secret(request):
    if not session_check(request):
        return redirect('secrets:index')

    result = Secret.objects.post_secret(request)

    if result:
        print_errors(request, result)

    return redirect('secrets:index')


def destroy(request, id):
    if not session_check(request):
        return redirect('secrets:index')
    else:
        Secret.objects.destroy_secret(request, id)

        return redirect('secrets:index')
def like(request, id):
    Secret.objects.like_secret(request, id)
    return redirect('secrets:index')

def index(request):
    if not session_check(request):
        return redirect('secrets:index')

    context = {
        'secrets': Secret.objects.all()[::-1]
    }

    return render(request, 'secrets/index.html', context)

def logout(request):
    request.session.clear()

    return redirect('login:index')
