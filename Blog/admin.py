from django.contrib import admin
from .models import Post , Category,Comment,Message , Like


class FilterByTitle(admin.SimpleListFilter):
    title = 'کلیدهای پرتکرار'
    parameter_name = "title"
    def lookups(self, request, model_admin):
        return (
        ('python' , 'پایتون'),
        ('django' , 'جنگو'),
    )
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title__icontains = self.value())

class CommentInline(admin.TabularInline):
    model = Comment
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title","author" , "status" , "published" , "show_image")
    list_editable = ("status","published")
    list_filter = ("status","published" , FilterByTitle)
    inlines = (CommentInline,)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Message)
admin.site.register(Like)
