from django.contrib import admin

from review.models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_display_links = ('pk', 'name')
    list_filter = ('category',)
    search_fields = ('name',)
    fields = ['name', 'category', 'description', 'pr_img']


admin.site.register(Product, ProductAdmin)
admin.site.register(Review)
