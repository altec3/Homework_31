from django.urls import path

from users import views

urlpatterns = [
    path('', views.UsersListView.as_view(), name='user'),
    path('create/', views.UserCreateView.as_view(), name='user_create'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='user_by_pk'),
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
    path('z/', views.UserTotalAdsView.as_view(), name='user_total_ads'),
]
