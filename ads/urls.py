from django.urls import path, include

from ads import views

urlpatterns = [
    path('', views.AdsView.as_view(), name='ad'),
    path('<int:pk>/', views.AdView.as_view(), name='ad_by_pk'),
]
