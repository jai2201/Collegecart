from django.shortcuts import render, redirect
from .models import Category , item, subcategory

def indexView(request):
	return render(request, 'index.html')


def adView(request):
	cat = Category.objects.all()
	sub = {}
	for z in cat:
		sub [(z.id)]=subcategory.objects.filter(category=z)
	print('sub',sub)
	return render(request, 'ad.html',  {'cat' : cat , 'sub': sub})
