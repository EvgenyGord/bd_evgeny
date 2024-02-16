from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),

    path('authors/', views.display_authors, name='display_authors'),
    path('authors/add/', views.add_author, name='add_author'),
    path('authors/<int:author_id>/edit/', views.edit_author, name='edit_author'),
    path('authors/<int:author_id>/delete/', views.delete_author, name='delete_author'),
    path('authors/report/', views.report_authors, name='report_authors'),
    path('authors/export-excel/', views.export_authors_to_excel, name='export_authors_to_excel'),
    path('execute-sql-query/', views.execute_sql_query, name='execute_sql_query'),
    path('export-sql-results-to-excel/', views.export_sql_results_to_excel, name='export_sql_results_to_excel'),




    path('employees/', views.display_employees, name='display_employees'),
    path('employees/add/', views.add_employee, name='add_employee'),
    path('employees/<int:employee_id>/edit/', views.edit_employee, name='edit_employee'),
    path('employees/<int:employee_id>/delete/', views.delete_employee, name='delete_employee'),
    path('employees/export-excel/', views.export_employees_to_excel, name='export_employees_to_excel'),
    path('employees/report/', views.report_employees, name='report_employees'),

    path('genres/', views.display_genres, name='display_genres'),
    path('genres/add/', views.add_genre, name='add_genre'),
    path('genres/<int:genre_id>/edit/', views.edit_genre, name='edit_genre'),
    path('genres/<int:genre_id>/delete/', views.delete_genre, name='delete_genre'),
    path('genres/export-excel/', views.export_genres_to_excel, name='export_genres_to_excel'),
    path('genres/report/', views.report_genres, name='report_genres'),

    path('subscribers/', views.display_subscribers, name='display_subscribers'),
    path('subscribers/add/', views.add_subscriber, name='add_subscriber'),
    path('subscribers/<int:subscriber_id>/edit/', views.edit_subscriber, name='edit_subscriber'),
    path('subscribers/<int:subscriber_id>/delete/', views.delete_subscriber, name='delete_subscriber'),
    path('subscribers/export-excel/', views.export_subscribers_to_excel, name='export_subscribers_to_excel'),
    path('subscribers/report/', views.report_subscribers, name='report_subscribers'),

    path('books/', views.display_books, name='display_books'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
    path('books/export-excel/', views.export_books_to_excel, name='export_books_to_excel'),
    path('books/report/', views.report_books, name='report_books'),

    path('book_distributions/', views.display_book_distributions, name='display_book_distributions'),
    path('book_distributions/add/', views.add_book_distribution, name='add_book_distribution'),
    path('book_distributions/<int:book_distribution_id>/edit/', views.edit_book_distribution, name='edit_book_distribution'),
    path('book_distributions/<int:book_distribution_id>/delete/', views.delete_book_distribution, name='delete_book_distribution'),
    path('book_distributions/export-excel/', views.export_book_distributions_to_excel, name='export_book_distributions_to_excel'),
    path('book_distributions/report/', views.report_book_distributions, name='report_book_distributions'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]