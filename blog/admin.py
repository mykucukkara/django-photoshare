from django.contrib import admin

# Register your models here.
from blog.models import Category
#admin panelde arayüz işlemleri
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']
admin.site.register(Category,CategoryAdmin)
