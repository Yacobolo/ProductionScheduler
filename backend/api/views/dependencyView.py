from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from api.services.dependency import DependencyService

dependency_service = DependencyService()

class DependencyTypesListView(APIView):
    def get(self, request, format=None):
        """
        List all dependency types.
        """
        result = dependency_service.get_all_dependency_types(request, format=None)
        return Response(result, status=result["code"])


class CreateUpdateDependencyTypesView(APIView):
    def post(self, request, format=None):
        """
        Create dependency types.
        """
        result = dependency_service.create_dependency_types(request, format=None)
        return Response(result, status=result["code"])

    def put(self, request, id, format=None):
        """
        Update dependency types
        """
        result = dependency_service.update_dependency_types(request, id, format=None)
        return Response(result, status=result["code"])

    
    def delete(self, request, id, format=None):
        """
        delete dependency types detail by id
        """
        result = dependency_service.delete_dependency_types(request, id, format=None)
        return Response(result, status=result["code"])
        


class DependencListView(APIView):
    def get(self, request, format=None):
        """
        List all dependency.
        """
        result = dependency_service.get_all_dependency(request, format=None)
        return Response(result, status=result["code"])


class CreateUpdateDependencView(APIView):
    def post(self, request, format=None):
        """
        Create dependency.
        """
        result = dependency_service.create_dependency(request, format=None)
        return Response(result, status=result["code"])

    def put(self, request, id, format=None):
        """
        Update dependency
        """
        result = dependency_service.update_dependency(request, id, format=None)
        return Response(result, status=result["code"])

    def get(self, request, id, format=None):
        """
        get dependency details by id
        """
        result = dependency_service.get_dependency_details_by_id(request, id, format=None)
        return Response(result, status=result["code"])
    
    def delete(self, request, id, format=None):
        """
        delete dependency detail by id
        """
        result = dependency_service.delete_dependency(request, id, format=None)
        return Response(result, status=result["code"])
        