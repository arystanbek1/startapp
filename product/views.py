from rest_framework.response import Response
from rest_framework.views import APIView
from product.serializer import OrganizationSerializer
from product.models import Organization


class OrganizationAPIView(APIView):
    def get(self, request):
        query = Organization.objects.all()
        serializer = OrganizationSerializer(query, many=True)
        return Response(serializer.data)


