import requests
from common import JSONLike


class RestClient:
    def __init__(self, rest_address: str):
        self._session = requests.session()
        self.rest_address = rest_address

    def query(self, request: str) -> JSONLike:
        response = self._session.get(url=self.rest_address + request)
        if response.status_code != 200:
            raise RuntimeError(
                f"Error when sending a query request.\n Request: {request}\n Response: {response})"
            )
        return response.json()
