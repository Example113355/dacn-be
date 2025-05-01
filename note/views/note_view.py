from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from note.exceptions import  NoteNotOwner
from note.models.note_model import Note
from note.serializers.note_serializer import NoteSerializer, UpdateNoteSerializer
from authentication.serializers.user_serializer import UserSerializer


class NoteView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Note.objects.filter(user=self.request.user).select_related("user")
    
    def get_serializer_class(self):
        if self.action == "update":
            return UpdateNoteSerializer
        return NoteSerializer
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        user_serializer = UserSerializer(request.user)
        
        return Response({
            "user": user_serializer.data,
            "notes": serializer.data
        }, status=status.HTTP_200_OK)
        
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        note_validated = serializer.validated_data
        
        note = Note.objects.get(id=note_validated.get("id"))
        
        if note.user != request.user:
            raise NoteNotOwner()
        
        note = serializer.save(user=request.user)
        
        return Response({
            "note": NoteSerializer(note).data
        }, status=status.HTTP_201_CREATED)
        
    def update(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        note_validated = serializer.validated_data
        
        note = Note.objects.get(id=note_validated.get("id"))
        
        if note.user != request.user:
            raise NoteNotOwner()
        
        note.title = note_validated.get("title")
        note.content = note_validated.get("content")
        note.save()
        
        return Response({
            "note": NoteSerializer(note).data
        }, status=status.HTTP_200_OK)