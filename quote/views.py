import logging
from concurrent.futures import as_completed

from requests_futures.sessions import FuturesSession
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import services
from .serializers import QuoteSerializer

session = FuturesSession()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("quote_views.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class KanyeWestTenQuotesView(APIView):
    """
    API view returns asynchronously 10 quotes by Kanye West with analysis of it
    from 'api.kanye.rest' API server.

    Analysis:
        - The quote itself
        - Number of letters
        - Number of vowels
        - Number of consonants
        - Frequency of letters
        - Average length of words
        - Three longest words
        (IF quote less than three words, it returns all words sorted by its length.)

    """

    serializer_class = QuoteSerializer

    def get(self, request):
        data = []
        try:
            futures = [
                session.get("https://api.kanye.rest/") for _ in range(10)
            ]
            logger.info("Received 10 quotes from server")
            for future in as_completed(futures):
                response = future.result()
                if response.status_code == 200:
                    quote = services.get_or_create_quote(
                        response.json()["quote"]
                    )
                    data.append(self.serializer_class(quote).data)
                    logger.info(
                        f'Got quote analysis for quote -> {response.json()["quote"]}'
                    )
                else:
                    logger.exception(
                        f"""Received response with status code
                        ({response.status_code}) -> {response.errors}
                        """
                    )
        except Exception as e:
            logger.exception(e)
            raise e
        return Response(data, status=status.HTTP_200_OK)
