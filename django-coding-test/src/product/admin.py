from django.contrib import admin
from .models import Product, ProductVariant, ProductImage, ProductVariantPrice, Variant


class AdminVariant(admin.ModelAdmin):
    list_display = ["title", "description", "active"]


admin.site.register(Variant, AdminVariant)


class AdminProduct(admin.ModelAdmin):
    list_display = ["title", "sku", "description"]


admin.site.register(Product, AdminProduct)


class AdminProductVariant(admin.ModelAdmin):
    list_display = ["variant_title", "variant", "product"]


admin.site.register(ProductVariant, AdminProductVariant)

admin.site.register(ProductImage)


class AdminVariantPrice(admin.ModelAdmin):
    list_display = [
        "product_variant_one",
        "product_variant_two",
        "product_variant_three",
        "price",
        "stock",
        "product",
    ]


admin.site.register(ProductVariantPrice, AdminVariantPrice)
