from rest_framework import serializers
from utils.notes import Note


class NoteSerializer(serializers.ModelSerializer):
    note_string = serializers.CharField(max_length=5)

    def validate_note_string(self, value):
        try:
            note = Note(value)
        except ValueError:
            raise serializers.ValidationError(f"Invalid note: {value}")
        return value

    def create(self, validated_data):
        note_string = validated_data.get("note_string")
        note = Note(note_string)
        return note

    def to_representation(self, instance):
        return {"note_string": instance.note_string}
