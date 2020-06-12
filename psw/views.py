from django.shortcuts import render
from rest_framework import generics, mixins, status

from psw.models import Exercice
from psw.serializers import ExerciceSerializer
# Create your views here.

class  ExerciceAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    "Exercice list and  View"
    lookup_field = 'id'
    serializer_class = ExerciceSerializer

    def get_queryset(self):
        qs = Exercice.objects.all()
        return qs

    def  post(self,request,*args,**kwargs):
        return  self.create(request,*args,**kwargs)



class  ExerciceRudView(generics.RetrieveUpdateDestroyAPIView):
    "Exercice Rud View"

    lookup_field = 'id'
    serializer_class = ExerciceSerializer

    def get_queryset(self):
         return  Exercice.objects.all()

