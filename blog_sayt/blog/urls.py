from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

urlpatterns = [
    path('article/<int:pk>/delete/',BlogDeleteView.as_view(),name='jek_delete'),
    path('article/<int:pk>/edit',BlogUpdateView.as_view(),name='jek_edit'),
    path('article/new/',BlogCreateView.as_view(),name='jek_new'),
    path('article/<int:pk>/',BlogDetailView.as_view(),name='jek_detail'),
    path('',BlogListView.as_view(),name='home')
]