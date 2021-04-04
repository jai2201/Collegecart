from django.urls import path
from . import views 
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
	path('login/',LoginView.as_view(),name="login"),
	path('logout/',LogoutView.as_view(next_page='login'),name="logout"),
	path('register/',views.registerView,name="register"),
	path('' ,views.indexView,name="index"),
	path('ad/' ,views.adView,name="ad"),
	path('post/',views.formView,name="post"),
	path('about/',views.aboutusView,name="about"),
]