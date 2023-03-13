from django.shortcuts import render
from rest_framework.views import APIView
from .models import Base
from .serializer import BaseSerializer
from rest_framework.response import Response

# Create your views here.
class LeadView(APIView):
    def get(self, request):
        output = [
            {
                "name": output.name,
                "message": output.message
            } for output in Lead.objects.all()
        ]
        return Response(output)

    def post(self, request):
        serializer = LeadSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)