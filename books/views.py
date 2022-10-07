from django.shortcuts import render, redirect
from.forms import UserRegisterForm
from django.contrib import messages
import books
from.models import Book
from.forms import EditBook
# Create your views here.

def login_page(request):
    # page = 'login'
    # # we dont want the user relogging in, so...
    # if request.user.is_authenticated:
    #     return redirect('home')

    # # making users to log in
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')

    #     #checking if the user exist or not
    #     try:
    #         user = User.objects.get(username=username)
    #     except:
    #         messages.error(request, 'User does not exist')

    #     #if the user exist
    #     user = authenticate(request, username=username, password=password)

    #     if user is not None:
    #         login(request,user)
    #         return redirect('home')
    #     else:
    #         messages.error(request, "Username OR password doses not exist" )

    # context = {'page':page}
    # return render(request, 'base/login_register.html', context)
    pass



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'books/register.html', {'form':form})











def home(request):
    return render(request, 'books/home.html')


def all_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books/all_books.html', context )



def book_detail(request, id):
    book = Book.objects.get(pk=id)
    context = {'book': book}
    return render(request, 'books/book_detail.html', context )


def add_book(request):
    # checking if the method is POST
    if request.method == 'POST':
        # getting all the data from the POST request
        data = request.POST
        # getting the image
        image = request.FILES.get('image-file')
        # creating and saving the book
        Book.objects.create(
           title = data['title'],
           author = data['author'],
           description = data['description'],
           isbn = data['isbn'],
           price = data['price'],
           image = image
        )
        # going to the home page
        return redirect('all-books')
    return render(request, 'books/add_book.html')
        

def update_book(request, id):
    book = Book.objects.get(pk=id)
    if request.method == 'POST':
        form = EditBook(request.POST, request.FILES, instance=book)

        if form.is_valid():
            form.save()
            return redirect('all-books')
    else:
        form = EditBook()
    return render(request, 'books/update_book.html', {'form':form})

        

def delete_book(request, id):
    if request.method == 'POST':
        book = Book.objects.get(pk=id)
        book.delete()
        return redirect('all-books')
    return render(request, 'books/delete_book.html')

