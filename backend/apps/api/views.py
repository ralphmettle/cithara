from rest_framework import views, status
from rest_framework.response import Response
from utils.notes import Note


class CheckEnharmonicView(views.APIView):
    """Check if two notes are enharmonic"""

    def post(self, request, *args, **kwargs):
        note1_string = request.data.get("note1")
        note2_string = request.data.get("note2")

        if not note1_string or not note2_string:
            return Response({"error": "Both 'note1' and 'note2' must be provided."})

        try:
            note1 = Note(note1_string)
            note2 = Note(note2_string)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        if note1.is_enharmonic(note2):
            return Response({"is_enharmonic": True})
        else:
            return Response({"is_enharmonic": False})
