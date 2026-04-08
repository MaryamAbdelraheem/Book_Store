from django.shortcuts import render

# Sample authors data
authors = [
    {
        'id': 1,
        'name': 'F. Scott Fitzgerald',
        'bio': 'F. Scott Fitzgerald was an American novelist, essayist, and screenwriter best known for his novel "The Great Gatsby". He is widely regarded as one of the greatest American writers of the 20th century.',
        'image': '/static/authors/fitzgerald.jpg',
        'birth_year': 1896,
        'death_year': 1940,
        'nationality': 'American',
        'books': 'The Great Gatsby, Tender Is the Night'
    },
    {
        'id': 2,
        'name': 'Harper Lee',
        'bio': 'Harper Lee was an American novelist known for her novel "To Kill a Mockingbird". She is one of the most widely read and taught authors in America.',
        'image': '/static/authors/harper-lee.jpg',
        'birth_year': 1926,
        'death_year': 2016,
        'nationality': 'American',
        'books': 'To Kill a Mockingbird, Go Set a Watchman'
    },
    {
        'id': 3,
        'name': 'George Orwell',
        'bio': 'George Orwell was an English novelist and essayist best known for his novels "1984" and "Animal Farm". His work is known for its social and political commentary.',
        'image': '/static/authors/orwell.jpg',
        'birth_year': 1903,
        'death_year': 1950,
        'nationality': 'British',
        'books': '1984, Animal Farm'
    },
    {
        'id': 4,
        'name': 'Jane Austen',
        'bio': 'Jane Austen was an English novelist known for her romantic fiction set among the British landed gentry. Her novels are extremely popular and have been adapted numerous times.',
        'image': '/static/authors/austen.jpg',
        'birth_year': 1775,
        'death_year': 1817,
        'nationality': 'British',
        'books': 'Pride and Prejudice, Sense and Sensibility'
    },
]


def index(request):
    return render(request, 'authors/index.html', {'authors': authors})


def show(request, author_id):
    selected_author = None
    for author in authors:
        if author['id'] == author_id:
            selected_author = author
            break
    return render(request, 'authors/show.html', {'author': selected_author})
