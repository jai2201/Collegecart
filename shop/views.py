from django.shortcuts import render, redirect
from .models import Category , item, subcategory
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def registerView(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
			form = UserCreationForm()	
	return render(request,'registration/register.html', {'form':form})

@login_required
def indexView(request):
	return render(request, 'index.html')

@login_required
def adView(request):
	cat = Category.objects.all()
	sub = {}
	for z in cat:
		sub [(z.id)]=subcategory.objects.filter(category=z)
	print('sub',sub)
	return render(request, 'ad.html',  {'cat' : cat , 'sub': sub})

@login_required
def formView(request):
	if request.method == "POST":
		form = ItemForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
	form = ItemForm()
	pht = item.objects.all()
	return render(request,'form.html', {'form':form , 'pht':pht } )

@login_required
def aboutusView(request):
	return render(request, 'aboutus.html')

