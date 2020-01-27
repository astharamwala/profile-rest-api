from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):

    def get(self, request, format=None):
        an_api = ['feature1', 'feature2', 'feature3']
        return Response({"message": "Hello", "an_api": an_api})
