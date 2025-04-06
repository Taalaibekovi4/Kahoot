from django.contrib import admin
from .models import School, Class, Level, Quiz, User

admin.site.register(School)
admin.site.register(Class)
admin.site.register(Level)
admin.site.register(Quiz)
admin.site.register(User)
