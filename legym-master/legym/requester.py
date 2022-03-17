import json

import requests

from .official import __api__
from .response import LegymResponse


class LegymRequester:
    """Legym API requester."""

    def __init__(self) -> None:
        """Read configurations."""
        self._headers = {"content-type": "application/json"}
        self._api_dict = __api__

    def __str__(self) -> str:
        return "<Legym Requester>"

    def __repr__(self) -> str:
        return "<Legym Requester>"

    def request(self, api_name: str, persist_path: str = "") -> LegymResponse:
        """Issue a request.

        Args:
            api_name: Name of API, to which the request is issued.
            persist_path: File path to persist response, default to "",
            in which case the response will not be persisted.

        Returns:
            Processed response.
        """
        api = self._api_dict[api_name]
        url = api["url"]
        method = api["method"]
        data = json.dumps(api["data"])

        if method == "get":
            response = requests.get(url, headers=self._headers)
        elif method == "post":
            response = requests.post(url, data, headers=self._headers)
        elif method == "put":
            response = requests.put(url, data, headers=self._headers)
        else:
            raise Exception("invalid request type")

        legym_response = LegymResponse(response, name=api_name)
        if persist_path != "":
            legym_response.persist()

        return legym_response

    def _update_api(self, api_name: str, new_data: dict) -> None:
        """Update data of API.

        Args:
            api_name: Name of API, of which the data will be updated.
            new_data: New data to add.
        """
        cur_data: dict = self._api_dict[api_name]["data"]
        cur_data.update(new_data)
