from django.urls import path

from selections import views

urlpatterns = [
    path('', views.SelectionsListView.as_view(), name='selections'),
    path('create/', views.SelectionCreateView.as_view(), name='selection_create'),
    path('<int:pk>/', views.SelectionDetailView.as_view(), name='selection_by_pk'),
    path('<int:pk>/update/', views.SelectionUpdateView.as_view(), name='selection_update'),
    path('<int:pk>/delete/', views.SelectionDeleteView.as_view(), name='selection_delete'),
]
