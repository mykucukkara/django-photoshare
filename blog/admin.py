from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from blog.models import Category, Blog


# admin panelde arayüz işlemleri
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'category', 'image_tag', 'status']
    list_filter = ['status']
    readonly_fields = ('image_tag',)


class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_blogs_count', 'related_blogs_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative blog count
        qs = Category.objects.add_related_count(
            qs,
            Blog,
            'category',
            'blogs_cumulative_count',
            cumulative=True)

        # Add non cumulative blog count
        qs = Category.objects.add_related_count(qs,
                                                Blog,
                                                'category',
                                                'blogs_count',
                                                cumulative=False)
        return qs

    def related_blogs_count(self, instance):
        return instance.blogs_count

    related_blogs_count.short_description = 'Related blogs (for this specific category)'

    def related_blogs_cumulative_count(self, instance):
        return instance.blogs_cumulative_count

    related_blogs_cumulative_count.short_description = 'Related blogs (in tree)'


admin.site.register(Category, CategoryAdmin2)
admin.site.register(Blog, BlogAdmin)
