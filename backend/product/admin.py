from django.contrib import admin
from .models import Product, ProductAttribute, ProductImages, Currency

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'currency', 'price', 'attributes')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductAttribute)
admin.site.register(ProductImages)
admin.site.register(Currency)
