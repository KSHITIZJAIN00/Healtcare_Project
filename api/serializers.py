from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Patient, Doctor, Mapping

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, data):
        user = User(username=data["username"])
        user.set_password(data["password"])
        user.save()
        return user

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"

class MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mapping
        fields = "__all__"
