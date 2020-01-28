from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from . import models, permissions
from .serializers import HelloSerializer, UserProfileSerializer, DemoSerializer


class HelloApiView(APIView):
    serializer_class = HelloSerializer

    def get(self, request, format=None):
        an_api = ['feature1', 'feature2', 'feature3']
        return Response({"message": "Hello", "an_api": an_api})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({"message": message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({"message": "Put"})

    def patch(self, request, pk=None):
        return Response({"message": "Patch"})

    def delete(self, request, pk=None):
        return Response({"message": "Delete"})


class HelloViewset(viewsets.ViewSet):
    serializable_class = HelloSerializer

    def list(self, request):
        a_viewset = ['feature1', 'feature2', 'feature3']
        return Response({"message": "Hello", "a_viewset": a_viewset})

    def retrieve(self, request, pk=None):
        return Response({"method": "GET"})

    def create(self, request):
        serialize = self.serializable_class(data=request.data)

        if serialize.is_valid():
            return Response({"name": serialize.validated_data["name"]})
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, req, pk=None):
        return Response({"method": "PUT"})

    def partial_update(self, req, pk=None):
        return Response({"method": "PATCH"})

    def destroy(self, req, pk=None):
        return Response({"method": "DELETE"})


class UserProfileViewset(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class DemoViewset(viewsets.ModelViewSet):
    serializer_class = DemoSerializer
    queryset = models.Demo.objects.all()
