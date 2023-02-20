from django.contrib import admin
from django.urls import path
from .views import BlocksView, StakingView

urlpatterns = [
    path('', BlocksView.as_view(), name= 'blocks'),
    path('staking/', StakingView.as_view(), name= 'staking'),
]
