from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import status
from .models import patient , doctor , mapping
from .serializers import userserializer , doctorserializer , patientserializer , mappingserializer

@api_view(["POST"])
def register(request):
    ser = userserializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response({"msg": "user made"})
    return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_patient(request):
    data = request.data
    data["user"] = request.user.id
    ser = patientserializer(data=data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data)
    return Response(ser.errors)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def all_patients(request):
    pts = patient.objects.filter(user=request.user)
    ser = patientserializer(pts, many=True)
    return Response(ser.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_doctor(request):
    ser = doctorserializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data)
    return Response(ser.errors)

@api_view(["GET"])
def all_doctors(request):
    docs = doctor.objects.all()
    ser = doctorserializer(docs, many=True)
    return Response(ser.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def map_doc(request):
    ser = mappingserializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data)
    return Response(ser.errors)

@api_view(["GET"])
def all_mappings(request):
    maps = mapping.objects.all()
    ser = mappingserializer(maps, many=True)
    return Response(ser.data)
