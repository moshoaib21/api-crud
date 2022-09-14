from dataclasses import fields
from rest_framework import serializers
from .models import hotel


class HotelSerislizer(serializers.ModelSerializer):
    class Meta:
        model = hotel
        fields = ['id','name','star','desc']
