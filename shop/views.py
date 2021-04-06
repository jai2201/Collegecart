from django.shortcuts import render, redirect
from .models import Category , item, subcategory
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
	img = item.objects.all()
	final = img.order_by('-published_on')
	return render(request, 'index.html',{'final':final})

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


@login_required
def detailView(request,item_id):
	img = item.objects.get(pk=item_id)
	return render(request, 'detail.html',{'img':img})


@login_required
def profileView(request):
	logged_in_user = request.user
	logged_in_user_items = item.objects.filter(user=logged_in_user)
	return render(request, 'profile.html', {'items':logged_in_user_items})

@login_required
def bookView(request):
	book_items = item.objects.filter(category__name = 'Books')
	return render(request, 'book.html', {'items':book_items})

@login_required
def electronicView(request):
	electronic_items = item.objects.filter(category__name = 'Electronics items')
	return render(request, 'electronic.html', {'items':electronic_items})

@login_required
def sportsView(request):
	sports_items = item.objects.filter(category__name = 'Sports material')
	return render(request, 'sport.html', {'items':sports_items})

@login_required
def musicView(request):
	music_items = item.objects.filter(category__name = 'Music items')
	return render(request, 'musical.html', {'items':music_items})

@login_required
def hostelView(request):
	hostel_items = item.objects.filter(category__name = 'Hostel stuff')
	return render(request, 'hostel.html', {'items':hostel_items})