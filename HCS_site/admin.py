from django.contrib import admin
from .models import News, Announcement, Complaint, Comments
# Register your models here.


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ("address_of_complaint", "date_of_complaint",)
    list_display_links = ("address_of_complaint",)
    list_filter = ("address_of_complaint", "date_of_complaint",)


class CommentsInline(admin.StackedInline):
    model = Comments
    extra = 1


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("name_of_news", "date_of_news",)
    list_display_links = ("name_of_news",)
    list_filter = ("date_of_news",)
    search_fields = ("name_of_news",)
    inlines = [CommentsInline]


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("name_of_commenter", "date_of_comment",)
    readonly_fields = ("name_of_commenter",)
    list_display_links = ("name_of_commenter", )
    list_filter = ("date_of_comment",)


admin.site.register(Announcement)
