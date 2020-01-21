from rest_framework.views import APIView
from rest_framework.response import  Response

class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'uses HTTP methods for function(get, post, patch,  put, delete)',
            'Is similar to a traditional django View',
            'Gives you the most control over application logic',
            'Is mapped manually to URLS',
        ]

        return Response({'message':'Hello', 'an_apiview':an_apiview})
