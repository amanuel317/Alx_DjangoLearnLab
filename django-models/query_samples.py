from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

# List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian

# Example usage
if __name__ == "__main__":
    author_books = get_books_by_author("J.K. Rowling")
    print(f"Books by J.K. Rowling: {[book.title for book in author_books]}")

    library_books = get_books_in_library("Central Library")
    print(f"Books in Central Library: {[book.title for book in library_books]}")

    librarian = get_librarian_for_library("Central Library")
    print(f"Librarian for Central Library: {librarian.name}")
