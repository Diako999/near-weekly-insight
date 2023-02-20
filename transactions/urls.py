from django.urls import path
from .views import TransactionsView, SwapsView

urlpatterns = [
   path('',TransactionsView.as_view(), name='transactions' ),
   path('swaps/', SwapsView.as_view(), name = 'swaps')
]
