from rest_framework import serializers
from .models import *


class EmployeeRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeRole
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'


class MFPTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MFPType
        fields = '__all__'


class MFPSerializer(serializers.ModelSerializer):
    class Meta:
        model = MFP
        fields = '__all__'


class MFPColourSerializer(serializers.ModelSerializer):
    class Meta:
        model = MFPColour
        fields = '__all__'


class MFPCartridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MFPCartridge
        fields = '__all__'


class PCSerializer(serializers.ModelSerializer):
    class Meta:
        model = PC
        fields = '__all__'


class RequestStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestStatus
        fields = '__all__'


class RequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = '__all__'
