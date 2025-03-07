from django.urls import path
from . import views

urlpatterns = [
    path('trails/', views.TrailCreateListView.as_view(), name='trail-create-list'),
    path('trails/<int:pk>/', views.TrailRetrieveUpdateDestroyView.as_view(), name='trail-detail-view')
]