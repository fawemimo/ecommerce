from django.contrib import admin
from .models import *
from .tasks import *


class ProductOnPromotionAdmin(admin.StackedInline):
    model = Promotion.products_on_promotion.through
    extra = 4
    raw_id_fields = ("products_inventory_id",)


class ProductInventoryList(admin.ModelAdmin):
    model = Promotion
    inlines = [ProductOnPromotionAdmin]
    list_display = ("name", "is_active", "promo_start", "promo_end")

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        promotion_prices.delay(obj.promo_reduction, obj.id)


admin.site.register(Promotion, ProductInventoryList)
admin.site.register(Coupon)
