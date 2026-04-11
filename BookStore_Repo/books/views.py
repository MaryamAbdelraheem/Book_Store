from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Book
from .forms import BookForm


def book_list(request):
    books = Book.objects.all().order_by('-created_at')
    return render(request, 'books/book_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES) 
        if form.is_valid():
            title = form.cleaned_data['title']

            # Check unique title
            if Book.objects.filter(title__iexact=title).exists():
                form.add_error('title', 'A book with this title already exists.')
                return render(request, 'books/book_form.html', {'form': form, 'action': 'Create'})

            Book.objects.create(
                title=title,
                brief=form.cleaned_data['brief'],
                image=form.cleaned_data.get('image'),  
                no_of_page=form.cleaned_data['no_of_page'],
                price=form.cleaned_data['price'],
            )
            messages.success(request, 'Book created successfully!')
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form, 'action': 'Create'})


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)  
        if form.is_valid():
            title = form.cleaned_data['title']

            # Check unique title — exclude current book
            if Book.objects.filter(title__iexact=title).exclude(pk=book.pk).exists():
                form.add_error('title', 'A book with this title already exists.')
                return render(request, 'books/book_form.html', {'form': form, 'action': 'Update', 'book': book})

            book.title = title
            book.brief = form.cleaned_data['brief']
            book.no_of_page = form.cleaned_data['no_of_page']
            book.price = form.cleaned_data['price']

            # ✅ Only update image if a new one was uploaded
            if form.cleaned_data.get('image'):
                book.image = form.cleaned_data['image']

            book.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('book_list')
    else:
        # ✅ Pre-fill form with current book data
        form = BookForm(initial={
            'title': book.title,
            'brief': book.brief,
            'no_of_page': book.no_of_page,
            'price': book.price,
        })
    return render(request, 'books/book_form.html', {'form': form, 'action': 'Update', 'book': book})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})