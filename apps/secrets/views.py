from django.shortcuts import render, HttpResponse, redirect
from models import User, Secret
from django.contrib import messages
from django.db.models import Count
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
        'secrets': Secret.objects.order_by('-created_at')[:10],
        'logged_in_user': User.objects.get(id=request.session['user']['user_id']),
    }

    return render(request, 'secrets/index.html', context)

def hotsecrets(request):
    if not session_check(request):
        return redirect('secrets:index')

    context = {
        'secrets': Secret.objects.annotate(num_HOT=Count('likes')).order_by('-num_HOT'),
        'logged_in_user': User.objects.get(id=request.session['user']['user_id']),
    }

    return render(request, 'secrets/hotsecrets.html', context)
def logout(request):
    request.session.clear()

    return redirect('login:index')
