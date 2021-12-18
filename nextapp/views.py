from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Movie, Actor
from .serializers import MovieSerializer, ActorSerializer

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    @action(detail=True, methods=['GET'])
    def actor(self, request, *args, **kwargs):
        kino = self.get_object()
        serializer = ActorSerializer(kino.actor.all(), many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def actors(self, request, *args, **kwargs):
        kino = self.get_object()
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        a = Actor.objects.last()
        kino.actor.add(a)
        kino.save()
        return Response(serializer.data)

class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer