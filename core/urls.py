from django.contrib import admin
from django.urls import path
from products import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.ProductListView.as_view(), name='products'),
]
