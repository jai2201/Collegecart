from django.urls import path
from . import views 
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
	path('' ,views.indexView,name="index"),
	path('ad/' ,views.adView,name="ad"),
]