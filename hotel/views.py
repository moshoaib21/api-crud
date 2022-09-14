from pickle import FALSE
from urllib import response
from django.http import JsonResponse
from .models import  hotel
from .serializers import HotelSerislizer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def hotel_list(request ,format=None):
    if request.method == 'GET':
        Hotel=hotel.objects.all()
        serializer=HotelSerislizer(Hotel,many=True)
        return JsonResponse({'hotel':serializer.data})

    if request.method == 'POST':
        serializer=HotelSerislizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
@api_view(['GET','PUT','DELETE'])
def hotel_details(request,id,format=None):
    try:
        Hotel=hotel.objects.get(pk=id)
    except hotel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET':
        serializer=HotelSerislizer(Hotel)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = HotelSerislizer(Hotel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Hotel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


