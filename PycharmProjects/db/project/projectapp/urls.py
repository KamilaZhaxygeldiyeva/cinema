from  django.urls import path
from . import views
urlpatterns=[

    #path('', views.main, name='main'),
    path('schedule/', views.schedule, name='schedule'),
    path('reserve',  views.reserve, name='reserve'),

]
