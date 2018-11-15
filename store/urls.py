from django.conf.urls import url
from .views import view_books, view_cached_books, create_book
 
 
urlpatterns = [
    url(r'^books/$', view_books),
    url(r'^books/cache/$', view_cached_books),
    url(r'^books/create/$', create_book)
]