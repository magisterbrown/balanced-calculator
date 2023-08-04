from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

@api_view(['GET'])
def add_numbers(request: Request) -> Response:
    return Response({'action': 'sumed'})

