from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "title",
            "num_page",
            "isbn13",
        ]
        extra_kwargs = {
            "isbn13":{"required": False},
        }