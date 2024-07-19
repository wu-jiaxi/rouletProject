from django.urls import path
from .views import ItemListCreateAPIView, ItemDetailAPIView, TicketListCreateAPIView, TicketDetailAPIView

urlpatterns = [
    path('items/', ItemListCreateAPIView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemDetailAPIView.as_view(), name='item-detail'),
    path('tickets/', TicketListCreateAPIView.as_view(), name='ticket-list-create'),
    path('tickets/<str:pk>/', TicketDetailAPIView.as_view(), name='ticket-detail'),
]
