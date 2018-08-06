from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
'''
from .forms import LoginForm
# Create your views here.
def login_view(request):
    if request.method =='POST':
        form = LoginForm(request.POST)
        rz
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next')
                if next_url:
                    return HttpResponseRedirect(next_url)
                return(HttpResponse('youpi'))
    else:
        form = LoginForm()

    return render(request, 'accounts/name.html', {'form': form})
'''

def logout_view(request):
    logout(request)
    return(HttpResponseRedirect(reverse('autre:index')))

@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})
        
