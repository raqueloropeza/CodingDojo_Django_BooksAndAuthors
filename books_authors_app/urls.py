from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('books', views.addbook),
    path('book_info/<int:book_id>',views.book_info),
    path('add_author/<int:books_id>', views.addauthor),
    path('authors',views.authors),
    path('newauthor', views.newauthor),
    path('author_info/<int:author_id>', views.author_info),
    path('add_book/<int:authors_id>', views.newbook),
]