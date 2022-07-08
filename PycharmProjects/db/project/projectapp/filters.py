import django_filters
from .models import *
from django_filters import DateFilter
class ScheduleFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='start_time', lookup_expr='date')

    class Meta:
        model=Schedule
        fields ='__all__'
        exclude = ['start_time']