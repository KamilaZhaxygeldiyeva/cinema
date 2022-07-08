
from django.db import models
from django.http import request
from django.urls import reverse
from multiselectfield import MultiSelectField
import datetime
from  django.core.validators import MaxValueValidator,MinValueValidator
from django.conf import settings
from django_countries.fields import CountryField
# Create your models here.

from django.utils.translation import gettext as _


import main
YEAR_CHOICES = [(r,r) for r in range(1984, datetime.date.today().year+1)]




class Discount(models.Model):
     discount_id = models.AutoField(primary_key=True)
     type_name = models.CharField(max_length=10, null=False)
     percent = models.IntegerField(null=False)

     def __str__(self):
         return self.type_name


class Hall(models.Model):
    hall_id= models.AutoField(primary_key=True)
    capacity = models.IntegerField()

    def __str__(self):
        return str(self.hall_id)


class RowOfHall(models.Model):
    row_id= models.AutoField(primary_key=True)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    number=models.IntegerField(null=False)

    def __str__(self):
        return str(self.number)


class Seat(models.Model):
    seat_id = models.AutoField(primary_key=True)
    row = models.ForeignKey(RowOfHall, on_delete=models.CASCADE)
    number = models.IntegerField(null=False)

    def __str__(self):
        return str(self.seat_id)


class Movie(models.Model):
    Боевик= 'Боевик'
    Комедия = 'Комедия'
    Приключения= 'Приключения'
    Мультфильм= 'Мультфильм'
    Ужасы= 'Ужасы'
    Спорт= 'Спорт'
    Фантастика= 'Фантастика'
    Фэнтези= 'Фэнтези'
    Триллер='Триллер'
    Детектив= 'Детектив'
    История= 'История'
    ДокументальныйФильм= 'Документальный фильм'
    Семейный= 'Семейный'
    Драма ='Драма'
    genre_in_choices =[
        (Боевик, 'Боевик'),
        (Комедия,'Комедия'),
        (Приключения,'Приключения'),
        (Мультфильм,'Мультфильм'),
        (Ужасы,'Ужасы'),
        (Спорт,'Спорт'),
        (Фантастика,'Фантастика'),
        (Фэнтези,'Фэнтези'),
        (Триллер,'Триллер'),
        (Детектив,'Детектив'),
        (История,'История'),
        (ДокументальныйФильм,'Документальный фильм'),
        (Семейный, 'Семейный'),
        (Драма , 'Драма'),

    ]
    movie_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    image = models.ImageField()#upload_to='movie')
    year = models.IntegerField(_('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    country = CountryField(multiple=True)
    during_time=models.DurationField()#IntegerField()

    genre = MultiSelectField(
        max_choices=5,
        choices=genre_in_choices,
    )
    description= models.TextField()

    rating = models.DecimalField(decimal_places=2, max_digits=4)#FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

    def __str__(self):
        return self.name
    class Meta:
        ordering=['name']
    def get_absolute_url(self):
        return reverse('movie', kwargs={'movie_slug': self.slug})

class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    price = models.FloatField()
    start_time= models.DateTimeField()

    def __str__(self):
        return str(self.schedule_id)

    '''def get_absolute_url(self):
        return reverse('schedule', kwargs={'pk': self.pk})
'''

class Payment(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, blank=True)
    shed_id = models.ForeignKey(Schedule,on_delete=models.CASCADE, blank=True)
    type = models.ForeignKey(Payment, on_delete=models.CASCADE, default=1)
    payment = models.ImageField(upload_to='picture')

    def __str__(self):
        return str(self.reservation_id)