
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect, render, get_object_or_404
from .forms import UserForm
from book.models import Book

# Create a register view for new account.
def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                # redirecting user into book list
                return redirect('book:book_list')
    
    context = {
        "form" : form,
        }
    
    return render(request, 'account/register.html', context)

# Create a login user view so they can login
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                # redirecting user into book list
                return redirect('book:book_list')
            else:
                return render(request, 'account/login.html', {'error_message' : 'Your account has been disabled'})

        else:
            return render(request, 'account/login.html', {'error_message' : 'Invalid Username or Password'})
    
    return render(request, 'account/login.html')

# Create a logout view for logout
def logout_user(request):
    logout(request)
    return redirect('account:login_user')