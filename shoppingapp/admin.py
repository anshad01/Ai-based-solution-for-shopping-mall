from django.contrib import admin
from shoppingapp import models

# Register your models here.


admin.site.register(models.Login)
admin.site.register(models.shopkeeper)
admin.site.register(models.User)
admin.site.register(models.Schedule)
admin.site.register(models.Appointment)
