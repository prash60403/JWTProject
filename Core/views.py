from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

@api_view(['GET'])
def Home(request):
    return Response("Hello world")
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def MyProtectedView(request):
    return Response("You have granted acces to this protected view.")
