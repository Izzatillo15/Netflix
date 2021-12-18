from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
    def validate_imdb(self,qiymat ):
        if self.qiymat < 2.0:
            raise ValidationError(detail="Bunaqa reytingda kino yo'q")
        return qiymat
    def validate_genre(self, qiymat):
        if len(qiymat) < 5:
            raise ValidationError(detail="Bu janrda kino yoq")
        return qiymat





class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
