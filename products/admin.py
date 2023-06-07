from django.contrib import admin
from .models import Product
from .models import Offer

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock")

class OffersAdmin(admin.ModelAdmin):
    list_display = ("code", "discount")

admin.site.register(Product, ProductsAdmin)
admin.site.register(Offer, OffersAdmin)