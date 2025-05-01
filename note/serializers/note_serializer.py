from rest_framework import serializers

from note.models.note_model import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ("id", "title", "content")


class UpdateNoteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    
    class Meta:
        model = Note
        fields = ("id", "title", "content")