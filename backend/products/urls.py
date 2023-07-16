from django.urls import path

from . import views

urlpatterns = [
    path('all-categories/', views.AllCategories.as_view(), name='all_categories'),
    path('all-products/', views.AllProducts.as_view(), name='all_products'),
    path('latest-products/', views.LatestProducts.as_view(), name='latest_products'),
    path('search/', views.search_products, name='search_products'),
    path('<slug:category_slug>/', views.CategoryDetail.as_view(), name='category_detail'),
    path('<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view(), name='product_detail'),
    path('check/check/check-products/', views.check_products, name='check_products'),
]
