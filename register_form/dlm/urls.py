from django.urls  import path,re_path

from . import views

urlpatterns = [
	path('',views.homePageView,name="home"),
	path('dashboard/',views.dashPageView,name="dashboard"),
	path('logout/',views.logout,name="logout"),
	re_path(r"filedetails/(?P<date>[\w\-]{10})/$",views.filedetails,name="filedetails"),
	re_path(r"viewfilecontents/(?P<filename>[\w\.\/\-]+)/$",views.viewfilecontents,name="filecontents")
]