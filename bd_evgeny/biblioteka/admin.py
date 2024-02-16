from django.contrib import admin
from .models import Author, Book, BookDistribution, Employee, Genre, Subscriber

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookDistribution)
admin.site.register(Employee)
admin.site.register(Genre)
admin.site.register(Subscriber)


