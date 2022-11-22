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
		forms = Formfillup.objects.filter(step=1)
		return render(request, 'app/deptDashboard.html', {'forms': forms})
	if user.is_staff and user.username == 'provost':
		forms = Formfillup.objects.filter(step=2)
		return render(request, 'app/hallDashboard.html', {'forms': forms})
	if user.is_staff and user.username == 'register':
		forms = Formfillup.objects.filter(step=3)
		return render(request, 'app/adminDashboard.html', {'forms': forms})
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
    return render(request, 'app/form.html', {'form': form})


def view_form(request):
    forms = Formfillup.objects.all()
    return render(request, 'app/form_list.html', {'forms': forms})

def change_step(request, form_id):
	form = Formfillup.objects.filter(id=form_id).last()
	form.step = int(form.step) + 1
	form.save()
	return redirect('index')


def add_payment(request, form_id):
	form = Formfillup.objects.filter(id=form_id).last()
	if request.method == 'POST':
		amount = request.POST.get('amount')
		form = Formfillup.objects.filter(id=form_id).last()
		form.payable_amount = float(amount)
		form.save()
		return redirect('index')
	return render(request, 'app/add_amount.html', {'form': form})