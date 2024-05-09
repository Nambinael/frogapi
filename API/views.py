from django.shortcuts import render
from .serializers import *
from .models import *

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, viewsets


class EmployeeRoleViewSet(viewsets.ModelViewSet):
    queryset = EmployeeRole.objects.all()
    serializer_class = EmployeeRoleSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class MapViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class MFPTypeViewSet(viewsets.ModelViewSet):
    queryset = MFPType.objects.all()
    serializer_class = MFPTypeSerializer


class MFPViewSet(viewsets.ModelViewSet):
    queryset = MFP.objects.all()
    serializer_class = MFPSerializer


class MFPColourViewSet(viewsets.ModelViewSet):
    queryset = MFPColour.objects.all()
    serializer_class = MFPColourSerializer


class MFPCartridgeViewSet(viewsets.ModelViewSet):
    queryset = MFPCartridge.objects.all()
    serializer_class = MFPCartridgeSerializer


class PCViewSet(viewsets.ModelViewSet):
    queryset = PC.objects.all()
    serializer_class = PCSerializer


class RequestStatusViewSet(viewsets.ModelViewSet):
    queryset = RequestStatus.objects.all()
    serializer_class = RequestStatusSerializer


class RequestsViewSet(viewsets.ModelViewSet):
    queryset = Requests.objects.all()
    serializer_class = RequestsSerializer
