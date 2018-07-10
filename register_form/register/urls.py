from django.urls  import path

from . import views

urlpatterns = [
	path('',views.registerUser,name="register"),
	path('success/',views.storeRegisterUser,name="success") ,
]