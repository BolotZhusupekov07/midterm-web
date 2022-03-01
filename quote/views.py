import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import services
from .serializers import QuoteSerializer


class KanyeWestTenQuotesView(APIView):
    def get(self, request):
        data = []
        for _ in range(10):
            req = requests.get("https://api.kanye.rest/")
            quote = services.get_or_create_quote(req.json()["quote"])
            data.append(QuoteSerializer(quote).data)
        return Response(data, status=status.HTTP_200_OK)
