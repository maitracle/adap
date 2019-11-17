from rest_framework.response import Response
from rest_framework.views import APIView


class DummyView(APIView):

    def get(self, request, format=None, *args, **kwargs):
        return Response({'message': 'dumb response!!'})
