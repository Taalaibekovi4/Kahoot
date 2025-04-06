from rest_framework import serializers
from .models import School, Class, Level, Quiz, User

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'name', 'students']

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['id', 'title', 'participants']

class SchoolSerializer(serializers.ModelSerializer):
    classes = ClassSerializer(many=True)
    levels = LevelSerializer(many=True)

    class Meta:
        model = School
        fields = ['id', 'name', 'classes', 'levels']

class QuizSerializer(serializers.ModelSerializer):
    winners = serializers.JSONField()

    class Meta:
        model = Quiz
        fields = ['id', 'quiz_name', 'level', 'date', 'winners']

class UserSerializer(serializers.ModelSerializer):
    schools = SchoolSerializer(many=True)

    class Meta:
        model = User
        fields = ['name', 'avatar', 'schools']
