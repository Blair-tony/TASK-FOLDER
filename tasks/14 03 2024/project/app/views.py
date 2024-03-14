from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import View
from django.views.generic import ListView,DetailView
from django.core import serializers
from .models import Book,Library

def view1(request):
    return HttpResponse("hi my name is blair")

def book_list(request):
    books=Book.objects.all()
    return render(request,'index.html',{'data':books})

def details(request,pk):
    book_details = Book.objects.get(pk=pk)

    context={
        'Book':book_details
        }
    return render(request,'details.html',context)

class BookDetailView(DetailView):
    model=Library
    template_name='library.html'
    context_object_name='Library'

class BookListViews(ListView):
    model=Book
    template_name="book_list.html"
    context_object_name="books"

class Librarylistview(ListView):
    model=Library
    template_name="list.html"
    context_object_name="Librarys"
