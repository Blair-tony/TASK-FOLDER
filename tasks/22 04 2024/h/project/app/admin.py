from django.contrib import admin

# Register your models here.
from .models import Role,car,Tag,Snippet

admin.site.register(Role)
admin.site.register(Snippet)
admin.site.register(car)
admin.site.register(Tag)