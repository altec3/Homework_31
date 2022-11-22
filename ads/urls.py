from django.urls import path

from ads import views

urlpatterns = [
    path('<int:pk>/upload_image/', views.AdUploadImageView.as_view(), name='ad_upload_image'),
]
