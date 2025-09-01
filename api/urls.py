from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("auth/register/", views.register),
    path("auth/login/", TokenObtainPairView.as_view()),
    path("patients/", views.all_patients),
    path("patients/add/", views.add_patient),
    path("doctors/", views.all_doctors),
    path("doctors/add/", views.add_doctor),
    path("mappings/", views.all_mappings),
    path("mappings/add/", views.map_doc),
]
