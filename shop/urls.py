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
	path('profile/',views.profileView,name="profile"),
	path('books/',views.bookView,name="book"),
	path('hostel/',views.hostelView,name="hostel"),
	path('electronic/',views.electronicView,name="electronic"),
	path('sports/',views.sportsView,name="sports"),
	path('musical/',views.musicView,name="musical"),
	path('detail/<int:item_id>/',views.detailView,name="detail"),
]