from django.urls import path

from categories import views

urlpatterns = [
    path('', views.CategoriesListView.as_view(), name='cat'),
    path('create/', views.CategoryCreateView.as_view(), name='cat_create'),
    path('<int:pk>/', views.CategoryDetailView.as_view(), name='cat_by_pk'),
    path('<int:pk>/update/', views.CategoryUpdateView.as_view(), name='cat_update'),
    path('<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='cat_delete'),
]