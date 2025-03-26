from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Wallet
from .serializers import WalletSerializer

# Create your views here.
class WalletView(APIView):
    def get(self, request, wallet_id):
        wallet = get_object_or_404(Wallet, id=wallet_id)
        return Response(WalletSerializer(wallet).data)
    
class WalletOperationView(APIView):
    def post(self, request, wallet_id):
        wallet = get_object_or_404(Wallet, id=wallet_id)
        operation_type = request.data.get("operation_type")
        amount = request.data.get("amount")

        if not amount or amount <= 0:
            return Response({"error": "Invalid amount"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            if operation_type == "DEPOSIT":
                wallet.deposit(amount)
            elif operation_type == "WITHDRAW":
                wallet.withdraw(amount)
            else:
                return Response({"error": "Invalid operation type"}, status=status.HTTP_400_BAD_REQUEST)
            
            return Response(WalletSerializer(wallet).data)
        except ValueError as e:
            return Response({"error":str(e)}, status = status.HTTP_400_BAD_REQUEST)
        
class WalletListView(ListAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class WalletCreateView(CreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer