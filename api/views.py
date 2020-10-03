from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from api.serializers import GhostpostSerializer
from ghostpost_app.models import Ghostpost
# Create your views here.


class GhostViewSet(viewsets.ModelViewSet):
    queryset = Ghostpost.objects.all().order_by("-id")
    serializer_class = GhostpostSerializer

  
@api_view(['PUT'])
def vote( request, id):
    post = Ghostpost.objects.get(id=id)
    serializer= GhostpostSerializer(post,data=request.data)
    if serializer.is_valid():
        print(post)
        serializer.save()
        return Response(serializer.data)
@api_view(['GET'])
def BoastView(request):
    post = Ghostpost.objects.filter(isboast="BOAST").order_by("-id")
    if request.method=="GET":
        serializer=GhostpostSerializer(post,many=True)
    
        return Response(serializer.data)

@api_view(['GET'])
def RoastView(request):
    post = Ghostpost.objects.filter(isboast="ROAST").order_by("-id")
    if request.method=="GET":
        serializer=GhostpostSerializer(post,many=True)
        
        return Response(serializer.data)


        

    



