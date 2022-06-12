from django.contrib import admin
from .models import Phone, CartItem, Cart, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('phoneName', 'phonePrice', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user',)


admin.site.register(Phone, ProductAdmin)
admin.site.register(CartItem)
admin.site.register(Cart, OrderAdmin)
admin.site.register(Category, CategoryAdmin)
