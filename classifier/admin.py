from django.contrib import admin

# Register your models here.
from .models import AllowedToken

admin.site.register(AllowedToken)
admin.site.register(Class)
admin.site.register(Feedback)
