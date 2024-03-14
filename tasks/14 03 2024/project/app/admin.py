from django.contrib import admin
from .models import Book,NewBook,Library
# Register your models here.
admin.site.register(Book)
admin.site.register(NewBook)
admin.site.register(Library)
