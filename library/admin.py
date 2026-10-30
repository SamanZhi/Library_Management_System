from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from library.models import Author, Book, BorrowedBook, Member


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "publication_date", "ISBN", "availability_status")
    search_fields = ("title", "ISBN")
    list_filter = ("availability_status",)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Member)
class MemberAdmin(UserAdmin):
    list_display = ("username", "email", "phone_number", "is_staff")
    fieldsets = list(UserAdmin.fieldsets)

    for index, (name, options) in enumerate(fieldsets):
        if name == "Personal info":
            fieldsets[index] = (
                name,
                {
                    **options,
                    "fields": options["fields"] + ("phone_number",),
                },
            )
            break
    fieldsets = tuple(fieldsets)
    add_fieldsets = (
        (
            UserAdmin.add_fieldsets[0][0],
            {
                **UserAdmin.add_fieldsets[0][1],
                "fields": UserAdmin.add_fieldsets[0][1]["fields"]
                + ("phone_number",),
            },
        ),
    )

@admin.register(BorrowedBook)
class BorrowBookAdmin(admin.ModelAdmin):
    list_display = ("book_title", "member_username", "borrow_date", "due_date", "return_date")
    search_fields = ("book__title", "member__username")
    list_filter = ("borrow_date", "return_date")
    list_select_related = ("book", "member")

    @admin.display(description="Book Title", ordering="book__title")
    def book_title(self, obj):
        return obj.book.title

    @admin.display(description="Member Username", ordering="member__username")
    def member_username(self, obj):
        if obj.member is None:
            return "Deleted member"
        return obj.member.username
            