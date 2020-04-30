from django.contrib import admin

# Register your models here.
from blog.models import Category, Blog


#admin panelde arayüz işlemleri
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'description','image_tag', 'status']
    list_filter = ['status']
    readonly_fields = ('image_tag',)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Blog,BlogAdmin)