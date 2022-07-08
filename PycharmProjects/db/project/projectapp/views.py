

from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse, request
from django.views.generic.edit import FormMixin

from .forms import Book
from .models import *
from .filters import *
from .models import *
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMessage

'''
def main(request):
    return render(request,'projectapp/main.html')
'''
def schedule(request):
    schedules = Schedule.objects.all()
    myFilter = ScheduleFilter(request.GET,queryset=schedules)
    schedules=myFilter.qs
    context = {'schedules':schedules, 'myFilter':myFilter}
    return render(request,'projectapp/schedule.html',context)

def reserve(request):
    #obj = (Schedule.objects.get(id=int:pk)).objects.values('schedule_id', 'price')

    if request.method == 'POST':
        username = request.user.username

        form = Book(request.POST, request.FILES)
        if form.is_valid():

            try:
                form.save()
                return redirect('reserve')
            except:
                form.add_error(None, 'Oшибка')

    else:
        form = Book()

    return render(request, 'projectapp/book.html', {'form': form})

