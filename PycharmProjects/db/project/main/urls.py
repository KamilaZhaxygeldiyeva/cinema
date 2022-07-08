from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from django.template.defaulttags import url
from django.urls import path, include
from . import views
from .views import RegisterUser, LoginUser

urlpatterns = [
    #path('', views.main_page, name='main'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('', views.today, name='today'),
    path('<int:pk>/info', views.NewsDetailView.as_view(), name='movie'),
    path('logout', LogoutView.as_view(template_name='main/logout.html'), name="logout"),
    path('', include('projectapp.urls')),

    #path("accounts/", include("django.contrib.auth.urls")),

]
#urlpatterns = [
#    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
#]
