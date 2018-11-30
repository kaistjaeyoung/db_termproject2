from django.contrib import admin
from .models import AirPlane, AirPort, Flight_captain, From_to, Time_line
# Register your models here.
admin.site.register(AirPlane)
admin.site.register(AirPort)
admin.site.register(Flight_captain)
admin.site.register(From_to)
admin.site.register(Time_line)
