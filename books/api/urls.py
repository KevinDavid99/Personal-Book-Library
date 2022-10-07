from django.urls import path
from.import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('', views.getRoutes),
    path('books/', views.get_books),
    path('books/<str:pk>/', views.getBooks),
]


urlpatterns = format_suffix_patterns(urlpatterns)