from django.urls import path
from.import views
urlpatterns = [
    path('' , views.home, name='home'),
    path('bookstore/', views.all_books, name='all-books'),
    path('book/<int:id>/',views.book_detail, name = 'book-detail'),
    path('add-book/', views.add_book, name='add-book'),
    path('update/<int:id>', views.update_book, name='update'),
    path('delete/<int:id>', views.delete_book, name='delete'),
]