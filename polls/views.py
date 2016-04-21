from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from .models import User
from .forms import UserForm
from django.shortcuts import redirect

def index(request):
    return render(request, "polls/index.html", {})

def registration(request):
  if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            polls_user = form.save(commit=False)
            polls_user.save()
            return redirect('index')
  else:
    form = UserForm()
  return render(request, 'polls/registration.html', {'form': form})

def sample(request):
  import random
  tickets = dict([User.objects.ticket, User.objects.first_name])
  random.choice(tickets.keys())
