from rest_framework import serializers
from django.contrib.auth.models import User
from .models import patient, doctor, mapping

class userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, data):
        user = User(username=data["username"])
        user.set_password(data["password"])
        user.save()
        return user

class patientserializer(serializers.ModelSerializer):
    class Meta:
        model = patient
        fields = "__all__"

class doctorserializer(serializers.ModelSerializer):
    class Meta:
        model = doctor
        fields = "__all__"

class mappingserializer(serializers.ModelSerializer):
    class Meta:
        model = mapping
        fields = "__all__"
