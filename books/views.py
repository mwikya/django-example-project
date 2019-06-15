from django.shortcuts import render

# Create your views here.
from django.views.generic import UpdateView,CreateView,ListView,DetailView,TemplateView,DeleteView
from books.models import Book,Author
from books.forms import BookForm

# def welcome(request):
# 	render("books/welcome.html")
class WelcomeView(TemplateView):
    template_name = "books/welcome.html"

class BookCreateView(CreateView):
    template_name = "books/book_create.html"
    model = Book
    form_class = BookForm

class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"

class BookDeleteView(DeleteView):
	model = Book
	template_name = "books/book_delete.html"

class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_details.html"

class BookUpdateView(UpdateView):
    model = Book
    template_name = "books/book_update.html"