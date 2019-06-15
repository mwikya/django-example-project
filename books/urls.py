from django.contrib import admin
from django.urls import path
from .views import BookCreateView,BookListView,BookUpdateView,BookDetailView,BookDeleteView

app_name = "books"
urlpatterns = [
    path("",BookListView.as_view(),name="book_list"),
    path("new/",BookCreateView.as_view(),name="book_create"),
    path("edit/<slug:book_id>/",BookUpdateView.as_view(),name="book_update"),
    path("details/<slug:book_id>/",BookDetailView.as_view(),name="book_details"),
    path("delete/<slug:book_id>/",BookDeleteView.as_view(),name="book_delete"),
]

