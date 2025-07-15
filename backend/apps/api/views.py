from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from cithara.core.scale.major_scale import MajorScale
from cithara.core.note import Note

class ScaleView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        note = request.query_params.get("note", "C")
        accidental = request.query_params.get("accidental")
        scale_type = request.query_params.get("type", "major")
        use_flats_str = request.query_params.get("use_flats")
        use_flats = True


        if use_flats_str and use_flats_str == "false":
            use_flats = False

        if accidental:
            pass

        if scale_type == "major":
            scale = MajorScale(root=Note(note), use_flats=use_flats)
            data = [degree.note.note_name for degree in scale.notes]
        else:
            return Response({"error": "Unsupported scale type"}, status=400)
        
        return Response({"scale": data})
