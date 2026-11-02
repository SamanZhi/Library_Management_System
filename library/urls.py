from django.urls import path

from library.views import BookListView

urlpatterns = [
    path("book-list/", BookListView.as_view()),
]