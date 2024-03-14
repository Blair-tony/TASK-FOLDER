
from django.urls import path
from . import views
from . views import *

urlpatterns = [
    path("view1/",views.view1),
    path("list/", book_list,name='book_list'),
    path('details/<int:pk>/',details,name="book_details"),
    path("detailview/<int:pk>/",views.BookDetailView.as_view(),name="library_details"),
    path("listview/<int:pk>/",views.BookListViews.as_view(),name="listview_details"),
    path("list2/", views.Librarylistview.as_view(),name='Library'),
]
