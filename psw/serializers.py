from rest_framework import serializers
from . models import Exercices, Courses, Corrections

class ExerciceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercices
        fields = "__all__"
    

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"



class CorrectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corrections
        fields = "__all__"