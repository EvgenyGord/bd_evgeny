from django import forms
from .models import Author, Employee, Genre, Subscriber, Book, BookDistribution

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['author_id', 'first_name', 'last_name', 'year_of_birth', 'year_of_death']
        labels = {
            'author_id': 'id',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'year_of_birth': 'Год рождения',
            'year_of_death': 'Год смерти',
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_id', 'first_name', 'last_name', 'position', 'phone_number']
        labels = {
            'employee_id': 'id',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'position': 'Должность',
            'phone_number': 'Номер телефона',
        }

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['genre_id', 'title', 'type', 'rating', 'description']
        labels = {
            'genre_id': 'id',
            'title': 'Название',
            'type': 'Тип',
            'rating': 'Рейтинг',
            'description': 'Описание',
        }

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['subscriber_id', 'first_name', 'last_name', 'address', 'phone_number']
        labels = {
            'subscriber_id': 'id',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'address': 'Адрес',
            'phone_number': 'Номер телефона',
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_id', 'title', 'year', 'fk_author', 'fk_genre']
        labels = {
            'book_id': 'id',
            'title': 'Название',
            'year': 'Год выпуска',
            'fk_author': 'Автор',
            'fk_genre': 'Жанр',
        }

class BookDistributionForm(forms.ModelForm):
    class Meta:
        model = BookDistribution
        fields = ['book_distribution_id', 'date_of_issue', 'return_date', 'fk_subscriber', 'fk_employee', 'fk_book']
        labels = {
            'book_distribution_id': 'id',
            'date_of_issue': 'Дата выпуска',
            'return_date': 'Дата возврата',
            'fk_subscriber': 'Абонент',
            'fk_employee': 'Сотрудник',
            'fk_book': 'Книга',
        }