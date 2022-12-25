from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from drf import views
from drf.views import CategoryList, ProductByCategory
from search.views import SearchProductInventory

# from drf.serializers import  *

router = routers.DefaultRouter()
router.register(
    r"api",
    views.AllProductsViewset,
    basename="allproducts",
)

router.register(
    r"product/(?P<slug>[^/.]+)",
    views.ProductInventoryViewset,
    basename="products",
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("demo/", include("demo.urls", namespace="demo")),
    path("", include(router.urls)),
    path("djninja/", include("djninja.urls")),
    path("search/<str:query>/", SearchProductInventory.as_view()),
    path("api/inventory/category/all", CategoryList.as_view()),
    path(
        "api/inventory/products/category/<str:query>/",
        ProductByCategory.as_view(),
    ),
]
