from django import forms
from .models import Book


class BookForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'})
    )
    brief = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter brief description'})
    )
    image = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )
    no_of_page = forms.IntegerField(
        min_value=1,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of pages'})
    )
    price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=0,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'})
    )

    def validate_unique_title(self, instance=None):
        title = self.cleaned_data.get('title')
        qs = Book.objects.filter(title__iexact=title)
        if instance:
            qs = qs.exclude(pk=instance.pk)  # exclude current book on update
        if qs.exists():
            raise forms.ValidationError("A book with this title already exists.")
        return title

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price

    def clean_no_of_page(self):
        pages = self.cleaned_data.get('no_of_page')
        if pages < 1:
            raise forms.ValidationError("Book must have at least 1 page.")
        return pages
    