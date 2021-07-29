from django.contrib import admin

# Register your models here.
from .models import User, Expert, Patient, UserProfil

admin.site.register(User)
admin.site.register(Expert)
admin.site.register(Patient)
admin.site.register(UserProfil)


