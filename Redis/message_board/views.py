from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MessageSerializer
from .models import *
from .tasks import *

# Create your views here.
@api_view(['GET'])
def get_messages(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response({ 'data': serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_message(request):
    serializer = MessageSerializer(data=request.data)
    add.delay(1, 2)
    
    if serializer.is_valid():
        serializer.save()
        return Response({ 'data': serializer.data}, status=status.HTTP_201_CREATED)
    return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_message(request, id):
    if id:
        message = Message.objects.get(id=id)
        message.delete()
    
    message = Message.objects.all()
    message.delete()

    return Response({ 'message': 'Message deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

