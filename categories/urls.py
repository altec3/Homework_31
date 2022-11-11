from django.urls import path

from categories import views

urlpatterns = [
    path('', views.CategoriesView.as_view(), name='cat'),
    path('<int:pk>/', views.CategoryView.as_view(), name='cat_by_pk'),
]