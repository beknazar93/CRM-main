from rest_framework import serializers
from .models import Employee,Client,SalesPipelineStage
from django import forms

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'stage', 'payment', 'price', 'sport_category', 'trainer', 'year',
                  'month', 'day', 'comment']





class SalesPipelineStageSerializer(serializers.ModelSerializer):
    clients = ClientSerializer(many=True, read_only=True)
    class Meta:
        model = SalesPipelineStage
        fields = '__all__'

