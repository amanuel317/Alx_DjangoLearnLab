from bookshelf.models import Book

# Create a new book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)

# Retrieve the book instance by title
book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")

# Update the book title
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated Title: {book.title}")

# Delete the book instance
book.delete()
print(Book.objects.all())
