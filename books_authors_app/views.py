from django.shortcuts import render, redirect
from .models import Books, Authors

#Main route that displays book information
def index(request):
    context = {
        "all_books": Books.objects.all(),
    }
    return render(request, "index.html", context)

#Add new book to table on main route
def addbook(request):
    new_book = Books.objects.create(title= request.POST['title'], desc= request.POST['desc'])
    return redirect("/")

#directs to route for specific book id selected and displays book information and authors related to record.
def book_info(request, book_id):
    context = {
        "books": Books.objects.get(id= book_id),
        "existing_authors": Books.objects.get(id=book_id).books.all(),
        "all_authors": Authors.objects.exclude(book=book_id),
    }
    print(context)
    return render(request, "bookview.html", context)

#add new author for specific book id selected. 
def addauthor(request, books_id):
    this_book = Books.objects.get(id= books_id)
    this_author = Authors.objects.get(id=int(request.POST['author']))
    this_book.books.add(this_author)
    return redirect(f"/book_info/{books_id}")

#displays all authors in database
def authors(request):
    context = {
        "all_authors": Authors.objects.all(),
    }
    return render(request, 'authors.html', context)

#add new author to database
def newauthor(request):
    new_author = Authors.objects.create(first_name= request.POST['firstname'], last_name= request.POST['lastname'], notes= request.POST['notes'])
    return redirect("/authors")
#displays information of specific author selected
def author_info(request, author_id):
    context = {
        "authors": Authors.objects.get(id= author_id),
        "existing_books": Authors.objects.get(id= author_id).book.all(),
        "all_books": Books.objects.exclude(books=author_id),
    }
    return render(request, "authorview.html", context)

#add new book to specific author id selected
def newbook(request, authors_id):
    this_author = Authors.objects.get(id= authors_id)
    this_book = Books.objects.get(id=int(request.POST['book']))
    this_author.book.add(this_book)
    return redirect(f"/author_info/{authors_id}")
