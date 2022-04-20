from django.contrib import admin
from django.urls import path, include
from company import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('inventory', views.InventoryGenericViewSet, basename='inventory')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.category_view),
    path('<int:pk>/', views.category_detail),
    path('company/', views.CompanyView.as_view()),
    path('company/<int:pk>/', views.CompanyDetailView.as_view()),
    path('', include(router.urls))

]
