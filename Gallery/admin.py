from django.contrib import admin
from Gallery.models import *
from django.db.models import QuerySet


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']
    list_display_links = ['name', ]
    list_per_page = 5
    search_fields = ['name', ]
    ordering = ['-id', ]


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']
    list_display_links = ['name', ]
    list_per_page = 5
    search_fields = ['name', ]
    filter = 'active'
    ordering = ['-id', ]
    actions = ['change_active', ]
    list_filter = ['name', 'category']


class ImageInlineAdmin(admin.TabularInline):
    model = ImagesInline
    extra = 0

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['name', 'active', 'slug', 'description', 'created']
    list_display_links = ['name', ]
    search_fields = ['name', ]
    list_filter = ['name', ]
    # list_filter = ['sub_category', 'category',
    #                'active']
    list_per_page = 10
    ordering = ['created', ]
    actions = ['change_active_true', 'change_active_false']
    prepopulated_fields = {'slug': ('name', )}
    inlines = [ImageInlineAdmin]

    @admin.action(description='Изменить на Активный')
    def change_active_true(self, request, qs: QuerySet):
        qs.update(active=True)

    @admin.action(description='Изменить на Неактивный')
    def change_active_false(self, request, qs: QuerySet):
        qs.update(active=False)

    def has_delete_permission(self, request, obj=None):
        return False
