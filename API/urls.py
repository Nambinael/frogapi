from rest_framework import routers
from django.urls import path, include
from .views import *

router = routers.DefaultRouter()

router.register(r'employeeroles', EmployeeRoleViewSet, basename='EmployeeRole')
router.register(r'employees', EmployeeViewSet, basename='Employee')
router.register(r'equipments', EquipmentViewSet, basename='Equipment')
router.register(r'mfptypes', MFPTypeViewSet, basename='MFPType')
router.register(r'mfp', MFPViewSet, basename='MFP')
router.register(r'mfpcolours', MFPColourViewSet, basename='MFPColour')
router.register(r'mptcartrige', MFPCartridgeViewSet, basename='MFPCartridge')
router.register(r'pc', PCViewSet, basename='PC')
router.register(r'requeststatuses', RequestStatusViewSet, basename='RequestStatus')
router.register(r'requests', RequestsViewSet, basename='Requests')

urlpatterns = router.urls