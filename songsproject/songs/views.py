from rest_framework import viewsets
from .models import Songs, RecordedSongs
from .serializers import SongsSerializer, RecordedSongsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404

class RecordedSongsViewSet(viewsets.ModelViewSet):
    queryset = RecordedSongs.objects.all()
    serializer_class = RecordedSongsSerializer
    permission_classes =[AllowAny]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        recordedsong = self.get_object()
        serializer = self.get_serializer(recordedsong, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        recordedsong = self.get_object()
        recordedsong.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SongsView(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = SongsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Song added successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        songs = Songs.objects.all()
        serializer = SongsSerializer(songs, many=True)
        return Response(serializer.data)
    
    def delete(self, request, id=None):
        if id is None:
            return Response({"error": "ID is required for deletion to be successful!!"}, status=status.HTTP_400_BAD_REQUEST)
        
        song = get_object_or_404(Songs, id=id)

        song.delete()
        return Response({"message": "Song deleted successfully"}, status=status.HTTP_204_NO_CONTENT)