from django.shortcuts import render
from rest_framework import generics, mixins, status
from rest_framework.permissions import IsAuthenticated

from psw.models import Exercices, Courses, Corrections
from psw.serializers import (ExerciceSerializer, CourseSerializer, 
                        CorrectionGetSerializer, CorrectionPostSerializer)
# Create your views here.

class  ExerciceAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    "Exercice list and  View"
    lookup_field = 'id'
    serializer_class = ExerciceSerializer
    #permission_classes = (IsAuthenticated, ) 

    def get_queryset(self):
        qs = Exercices.objects.all()
        return qs

    def  post(self,request,*args,**kwargs):
        return  self.create(request,*args,**kwargs)



class  ExerciceRudView(generics.RetrieveUpdateDestroyAPIView):
    "Exercice Rud View"
    #permission_classes = (IsAuthenticated, ) 
    lookup_field = 'id'
    serializer_class = ExerciceSerializer

    def get_queryset(self):
        return  Exercices.objects.all()




class  CourseAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    "Course list and  View"
    lookup_field = 'id'
    serializer_class = CourseSerializer
    #permission_classes = (IsAuthenticated, ) 

    def get_queryset(self):
        qs = Courses.objects.all()
        return qs

    def  post(self,request,*args,**kwargs):

        return  self.create(request,*args,**kwargs)



class  CourseRudView(generics.RetrieveUpdateDestroyAPIView):
    "Course Rud View"
    #permission_classes = (IsAuthenticated, ) 
    lookup_field = 'id'
    serializer_class = CourseSerializer

    def get_queryset(self):
         return  Courses.objects.all()



class CorrectionAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    "Correction list and  View"
    lookup_field = 'id'
    serializer_class = CorrectionPostSerializer
    
    #permission_classes = (IsAuthenticated, ) 

    def get_queryset(self):
        if self.request.method == 'GET':
            serializer_class = CorrectionGetSerializer
        qs = Corrections.objects.all()
        return qs

    def  post(self,request,*args,**kwargs):
        return  self.create(request,*args,**kwargs)



class CorrectionRudView(generics.RetrieveUpdateDestroyAPIView):
    "Correct Rud View"
    #permission_classes = (IsAuthenticated, ) 
    lookup_field = 'id'
    serializer_class = CorrectionPostSerializer

    def get_queryset(self):
        return  Corrections.objects.all()



