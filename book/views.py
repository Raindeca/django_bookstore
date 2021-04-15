# from django.contrib.auth import authenticate, login
# from django.contrib.auth import logout
# from django.shortcuts import render, get_object_or_404
# from django.db.models import Q
# from .models import Book
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Book



class IndexView(generic.ListView):
    template_name = 'book/books.html'
    context_object_name = 'all_books'

    def get_queryset(self):
        return Book.objects.all()

    def get(self, *args, **kwargs):
        if bool(self.request.user and self.request.user.is_authenticated):
            return super().get(*args, **kwargs)
        else:
            return redirect('account:login_user')

class DetailView(generic.DetailView):
    model = Book
    template_name = 'book/detail.html'

    def post(self, *args, **kwargs):
        pass



# Create your views here.
# def book_list(request):
#     if not request.user.is_authenticated:
#         return render(request, 'account/login.html')
#     else:
#         # books = Book.objects.all()
#         books = Book.objects.all()
#         query = request.GET.get("q")
        
#         if query:
#             books = books.filter(
#                 Q(book_title__icontains=query)
#             ).distinct()
#             return render(request, 'book/books.html', {
#                 'books' : books,
#             })
        
#         else:
#             return render(request, 'book/books.html', {'books' : books})

# def detail(request, book_id):
#     if not request.user.is_authenticated:
#         return render(request, 'account/login.html')
#     else:
#         user = request.user
#         book = get_object_or_404(Book, pk=book_id)
#         return render(request, 'book/detail.html', {
#             'book' : book,
#             'user' : user,
#         })