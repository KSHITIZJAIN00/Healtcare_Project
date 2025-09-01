from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import status
from .models import Patient, Doctor, Mapping
from .serializers import UserSerializer, PatientSerializer, DoctorSerializer, MappingSerializer

@api_view(["POST"])
def register(request):
    ser = UserSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response({"msg": "user made"})
    return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_patient(request):
    data = request.data
    data["user"] = request.user.id
    ser = PatientSerializer(data=data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data)
    return Response(ser.errors)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def all_patients(request):
    pts = Patient.objects.filter(user=request.user)
    ser = PatientSerializer(pts, many=True)
    return Response(ser.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_doctor(request):
    ser = DoctorSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data)
    return Response(ser.errors)

@api_view(["GET"])
def all_doctors(request):
    docs = Doctor.objects.all()
    ser = DoctorSerializer(docs, many=True)
    return Response(ser.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def map_doc(request):
    ser = MappingSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data)
    return Response(ser.errors)

@api_view(["GET"])
def all_mappings(request):
    maps = Mapping.objects.all()
    ser = MappingSerializer(maps, many=True)
    return Response(ser.data)
