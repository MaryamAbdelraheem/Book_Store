from django.shortcuts import render

# Create your views here.

books = [
    {
        'id': 1,
        'title': 'The Great Gatsby',
        'brief': 'A story about the American dream and the roaring twenties.',
        'image': '/static/books/the-great-gatsby.jpg',
        'no_of_page': 180,
        'price': 12.99
    },
    {
        'id': 2,
        'title': 'To Kill a Mockingbird',
        'brief': 'A tale of racial injustice and childhood innocence in the South.',
        'image': '/static/books/to-kill-a-mockingbird.jpg',
        'no_of_page': 281,
        'price': 14.99
    },
    {
        'id': 3,
        'title': '1984',
        'brief': 'A dystopian novel about totalitarianism and surveillance.',
        'image': '/static/books/1984.jpg',
        'no_of_page': 328,
        'price': 11.99
    },
    {
        'id': 4,
        'title': 'Pride and Prejudice',
        'brief': 'A romantic novel about manners, marriage and society in 19th century England.',
        'image': '/static/books/pride-and-prejudice.jpg',
        'no_of_page': 432,
        'price': 9.99
    },
]


def index(request):
    return render(request, 'books/index.html', {'books': books})


def show(request, book_id):
    selected_book = None
    for book in books:
        if book['id'] == book_id:
            selected_book = book
            break
    return render(request, 'books/show.html', {'book': selected_book})