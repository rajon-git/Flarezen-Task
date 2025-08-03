from django.shortcuts import render
from rest_framework import generics, status, permissions
from api.serializers import SubscriptionSerializer, ExchangeRateLogSerializer
from plan.models import Plan
from django.db import transaction
from datetime import date, timedelta
from .models import Subscription
from exchangerate.models import ExchangeRateLog
from rest_framework.response import Response
from rest_framework.views import APIView
import requests

# Create your views here.
class CreateSubscriptionView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SubscriptionSerializer

    def create(self, request, *args, **kwargs):
        plan_id = request.data.get('plan_id')
        print(f"------------{plan_id}---------")
        plan = Plan.objects.get(id=plan_id)

        with transaction.atomic():
            start_date = date.today()
            end_date = start_date + timedelta(days=plan.duration_days)

            subscription  = Subscription.objects.create(
                user=request.user,
                plan=plan,
                start_date=start_date,
                end_date=end_date,
                status='active'
            )
            serializer = self.get_serializer(subscription)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class UserSubscriptionsListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)
    
class CancelSubscriptionView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()

    def update(self,request, *args, **kwargs):
        sub_id = self.kwargs['subscription_id']
        print(f"<------{self.request.user}------>")
        print(f"<------{sub_id}------>")
        try:
            sub = Subscription.objects.get(id=sub_id, user=self.request.user)
            sub.status = 'cancelled'
            sub.save()
            serializer = self.get_serializer(sub)
            return Response({"message": "Subscription cancelled.", "data": serializer.data})
        except Subscription.DoesNotExist:
            return Response({"error": "Subscription not found."}, status=status.HTTP_404_NOT_FOUND)
        
class ExchangeRateView(APIView):
    def get(self, request):
        base = request.GET.get('base', 'USD')
        target = request.GET.get('target', 'BDT')
        
        try:
            data = requests.get(f"https://open.er-api.com/v6/latest/{base}").json()
            rate = data['rates'][target]
            
            ExchangeRateLog.objects.create(
                base_currency=base,
                target_currency=target,
                rate=rate
            )
            
            return Response({'rate': rate})
            
        except:
            return Response({'error': 'Failed to get rate'}, status=400)
        
def subscriptions_list(request):
    subscriptions = Subscription.objects.select_related('user', 'plan').all()
    return render(request,'subscriptions/subscriptions_list.html',{
        'subscriptions': subscriptions
    })