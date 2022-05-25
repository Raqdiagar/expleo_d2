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
    
class EntryDetailAPI(APIView):

    def get_user(self, request, pk):
        entry = get_object_or_404(Entry, pk=pk)
        return entry

    def get(self, request, pk):
        entry = self.get_user(request, pk)
        serializer = EntrySerializer(instance=entry)
        return Response(serializer.data)


    def put(self, request, pk):

        entry = get_object_or_404(Entry, pk=pk)
        serializer = EntrySerializer(instance=entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def delete(self, request, pk):
       
        user = get_object_or_404(Entry, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
