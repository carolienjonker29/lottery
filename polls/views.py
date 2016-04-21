from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from .models import User
from .forms import UserForm

def index(request):
    return render(request, "polls/index.html", {})

def registration(request):
  if request.method == "POST":
    form = UserForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.save()
    return redirect('confirmation')
  else:
    form = UserForm()
  return render(request, 'polls/registration.html', {'form': form})


def confirmation(request):
  return render(request, "polls/confirmation.html", {})

def sample(request):
  import random
  tickets = dict([User.objects.ticket, User.objects.first_name])
  random.choice(tickets.keys())
  return render(request, "polls/sample.html", {})
