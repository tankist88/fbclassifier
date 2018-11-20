from django.contrib import admin

# Register your models here.
from .models import AllowedToken, Class, Feedback

admin.site.register(AllowedToken)
admin.site.register(Class)
admin.site.register(Feedback)
