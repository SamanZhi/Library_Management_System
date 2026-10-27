from django.contrib import admin

from library.models import Author, Book, BorrowedBook, Member


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "publication_date", "ISBN", "availability_status"]
    search_fields = ["title", "ISBN"]
    list_filter = ["availability_status"]

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Member)
class MemberAdmin(admin.UserAdmin):
    pass

@admin.register(BorrowedBook)
class BorrowBookAdmin(admin.ModelAdmin):
    pass
