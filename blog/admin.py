from django.contrib import admin

# Register your models here.
from blog.models import Category, Blog


#admin panelde arayüz işlemleri
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']
admin.site.register(Category,CategoryAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status']
    list_filter = ['status']
admin.site.register(Blog,BlogAdmin)