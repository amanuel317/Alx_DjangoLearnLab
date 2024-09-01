from bookshelf.models import Book

# Delete the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion by retrieving all books
print(Book.objects.all())
