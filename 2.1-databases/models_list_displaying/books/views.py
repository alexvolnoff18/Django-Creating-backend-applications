from django.shortcuts import render
from django.core.paginator import Paginator

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, template, context)

def books_pagi_view(request):
    page_number = request.GET.get("page")
    books = Book.objects.all()
    paginator = Paginator(books)
    page = paginator.get_page(page_number)
    data = page.object_list

    context = {
        "books": books,
        'page': page,
    }
    return render(request, 'books_pagi_view.html', context)

# /books/<pub_date>/

# def bus_stations(request):
#     sys.path.append( "pagination" )
#     bus_stations = []

#     with open(settings.BUS_STATION_CSV, encoding = 'utf8', newline='') as csvfile:
#       reader = csv.DictReader(csvfile)
#       bus_stations = []
#       for row in reader:
#         bus_stations.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})


#     page_number = int(request.GET.get("page", 1))
#     paginator = Paginator(bus_stations, 10)
#     page = paginator.get_page(page_number)
#     data = page.object_list

#   # получите текущую страницу и передайте ее в контекст
#     # также передайте в контекст список станций на странице

#     context = {
#         'bus_stations': data,
#         'page': page,
#     }
#     return render(request, 'stations/index.html', context)