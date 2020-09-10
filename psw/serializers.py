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



class CorrectionGetSerializer(serializers.ModelSerializer):
    exercice = ExerciceSerializer(many=True)
    class Meta:
        model = Corrections
        fields = ('id' ,'name' ,'exercice' ,'correction_file','description')

class CorrectionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corrections
        fields = "__all__"