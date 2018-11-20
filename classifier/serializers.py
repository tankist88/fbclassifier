from rest_framework import serializers

from .models import Class, Feedback

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ('name', 'desc')

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('fclass', 'text')
