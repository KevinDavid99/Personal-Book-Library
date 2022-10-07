from rest_framework.serializers import ModelSerializer
from books.models import Book


class PostSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'