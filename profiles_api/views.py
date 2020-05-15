from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    def get(self, request, format=None):
        an_apiview = [
            'uses HTTP request to get resltd',
            'GET, POST, DELETE, UPDATE, PATCH'
        ]

        return Response({'message': 'Hello', 'an_apiView': an_apiview})
