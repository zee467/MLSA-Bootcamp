from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "book_genre")  # controls the fields to display
    search_fields = ["title"]

    def get_queryset(self, request):
        queryset = super(BookAdmin, self).get_queryset(request)
        queryset = queryset.order_by("id")
        return queryset

admin.site.register(Book, BookAdmin)
