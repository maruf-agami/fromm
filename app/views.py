from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Formfillup
from .forms import FormfillupForm

# Create your views here.

def index(request):
    user = request.user
    if user.is_staff and user.username == 'mannan':
        return render(request, 'app/deptDashboard.html')
    if user.is_staff and user.username == 'provost':
        return render(request, 'app/hallDashboard.html')
    if user.is_staff and user.username == 'register':
        return render(request, 'app/adminDashboard.html')
    return render(request, 'app/dashboard.html')
    # return HttpResponse('hello world!')


@login_required(login_url='/app/')
def add_formfillup(request):
	if request.method == 'POST':
		form = FormfillupForm(request.POST)
		if form.is_valid():
			p = form.save(commit=False)
			p.user = request.user
			p.save()
			return redirect(reverse('index'))
	else:
		form = FormfillupForm()
	return render(request, 'app/add_formfillup.html', {'form': form})



