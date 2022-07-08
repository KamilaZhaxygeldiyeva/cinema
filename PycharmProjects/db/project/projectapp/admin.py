from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.


admin.site.register(Discount)
admin.site.register(Hall)
admin.site.register(Movie)
admin.site.register(RowOfHall)
admin.site.register(Seat)
admin.site.register(Schedule)
admin.site.register(Payment)
admin.site.register(Reservation)

admin.site.site_header="Cinema"


