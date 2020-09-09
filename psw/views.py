from django.shortcuts import render
from rest_framework import generics, mixins, status
from rest_framework.permissions import IsAuthenticated

from psw.models import Exercice, Courses
from psw.serializers import ExerciceSerializer, CourseSerializer
# Create your views here.

class  ExerciceAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    "Exercice list and  View"
    lookup_field = 'id'
    serializer_class = ExerciceSerializer
    #permission_classes = (IsAuthenticated, ) 

    def get_queryset(self):
        qs = Exercice.objects.all()
        return qs

    def  post(self,request,*args,**kwargs):
        return  self.create(request,*args,**kwargs)



class  ExerciceRudView(generics.RetrieveUpdateDestroyAPIView):
    "Exercice Rud View"
    #permission_classes = (IsAuthenticated, ) 
    lookup_field = 'id'
    serializer_class = ExerciceSerializer

    def get_queryset(self):
         return  Exercice.objects.all()




class  CourseAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    "Exercice list and  View"
    lookup_field = 'id'
    serializer_class = CourseSerializer
    #permission_classes = (IsAuthenticated, ) 

    def get_queryset(self):
        qs = Courses.objects.all()
        return qs

    def  post(self,request,*args,**kwargs):
        return  self.create(request,*args,**kwargs)



class  CourseRudView(generics.RetrieveUpdateDestroyAPIView):
    "Exercice Rud View"
    #permission_classes = (IsAuthenticated, ) 
    lookup_field = 'id'
    serializer_class = CourseSerializer

    def get_queryset(self):
         return  Courses.objects.all()


