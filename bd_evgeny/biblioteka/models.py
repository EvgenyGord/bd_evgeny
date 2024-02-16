from django.db import models

class Author(models.Model):
    author_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    year_of_birth = models.CharField(max_length=32, null=True, blank=True)
    year_of_death = models.CharField(max_length=32, null=True, blank=True)
    class Meta:
        db_table = 'author'
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    position = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=32, null=True, blank=True)
    class Meta:
        db_table = 'employee'
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
class Subscriber(models.Model):
    subscriber_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    address = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    class Meta:
        db_table = 'subscriber'
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=32)
    type = models.CharField(max_length=32, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=128, null=True, blank=True)
    class Meta:
        db_table = 'genre'
    def __str__(self):
        return f'{self.title}'
class Book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=32)
    year = models.CharField(max_length=4)
    fk_author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    fk_genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        db_table = 'book'
    def __str__(self):
        return f'{self.title}'
class BookDistribution(models.Model):
    book_distribution_id = models.IntegerField(primary_key=True)
    date_of_issue = models.DateField()
    return_date = models.DateField()
    fk_subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE, null=True, blank=True)
    fk_employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    fk_book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        db_table = 'book_distribution'
    def __str__(self):
        return f'Дата выпуска: {self.date_of_issue} - Дата возврата: {self.return_date}'
