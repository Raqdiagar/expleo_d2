from http.client import responses
from rest_framework.views import APIView
from rest_framework.response import Response

from entries.models import EntryModel
from entries.api.serializers import EntrySerializer


class EntryListAPI(APIView):
    def get(self, request):    
        entries = EntryModel.objects.all()
        
        serilizer = EntrySerializer(entries, many=True)
        
        return Response(serilizer.data)
    
    def post(self, request):
        
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        
        return Response(status=400, data=serializer.errors)
    
    
