from django.shortcuts import render
from .main import Allosession
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    a = Allosession()
    return render(request, 'horaires/index.html', {'dico':a.dico})
