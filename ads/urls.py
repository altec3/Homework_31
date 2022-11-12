from django.urls import path

from ads import views

urlpatterns = [
    path('', views.AdsListView.as_view(), name='ad'),
    path('create/', views.AdCreateView.as_view(), name='ad_create'),
    path('<int:pk>/', views.AdDetailView.as_view(), name='ad_by_pk'),
    path('<int:pk>/update/', views.AdUpdateView.as_view(), name='ad_update'),
    path('<int:pk>/delete/', views.AdDeleteView.as_view(), name='ad_delete'),
    path('<int:pk>/upload_image/', views.AdUploadImageView.as_view(), name='ad_upload_image'),
]
