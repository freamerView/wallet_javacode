from django.urls import path
from .views import WalletView, WalletOperationView, WalletListView, WalletCreateView

urlpatterns = [
    path("", WalletListView.as_view(), name="wallet-list"),
    path("create/", WalletCreateView.as_view(), name='wallet-create'),
    path('<uuid:wallet_id>/', WalletView.as_view(), name='wallet-detail'),
    path('<uuid:wallet_id>/operation/', WalletOperationView.as_view(), name = "wallet-operation"),
]