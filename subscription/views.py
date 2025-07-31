from django.shortcuts import render
from rest_framework import generics, status, permissions
from api.serializers import SubscriptionSerializer
from plan.models import Plan
from django.db import transaction
from datetime import date, timedelta
from .models import Subscription
from rest_framework.response import Response

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