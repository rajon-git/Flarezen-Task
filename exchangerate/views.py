from django.shortcuts import render
import requests
from .models import ExchangeRateLog
from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import fetch_usd_to_bdt
from api.serializers import  ExchangeRateLogSerializer
from rest_framework import generics, status, permissions


# Create your views here.
class ExchangeRateView(APIView):
    def get(self, request):
        # base = request.GET.get('base', 'USD')
        # target = request.GET.get('target', 'BDT')

        fetch_usd_to_bdt.delay()
        latest = ExchangeRateLog.objects.last()

        if not latest:
            return Response({"message": "No exchange rate data yet."}, status=status.HTTP_204_NO_CONTENT)

        serializer = ExchangeRateLogSerializer(latest)
        return Response(serializer.data)
        
        # try:
        #     data = requests.get(f"https://open.er-api.com/v6/latest/{base}").json()
        #     rate = data['rates'][target]
            
        #     ExchangeRateLog.objects.create(
        #         base_currency=base,
        #         target_currency=target,
        #         rate=rate
        #     )
            
        #     return Response({'rate': rate})
            
        # except:
        #     return Response({'error': 'Failed to get rate'}, status=400)