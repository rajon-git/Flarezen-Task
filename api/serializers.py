from rest_framework import serializers
from plan.models import Plan
from subscription.models import Subscription
from exchangerate.models import ExchangeRateLog
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User 
        fields = ['username', 'email', 'password']

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'
class SubscriptionSerializer(serializers.ModelSerializer):
    user = RegisterSerializer(read_only=True)
    plan = PlanSerializer(read_only=True)
    class Meta:
        model = Subscription
        fields = '__all__'

class ExchangeRateLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRateLog
        fields = '__all__'