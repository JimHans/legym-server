import json
import os

import requests

from .exception import LegymException


class LegymResponse:
    """Response returned by Legym API."""

    def __init__(self, response: requests.Response, name: str) -> None:
        """Validate and parse raw response.

        Args:
            response: Raw response returned by Legym API.
            name: Name to mark this piece of response.
        """
        self.__response = response
        self.__name = name
        self.__parse_to_json()
        self.__ensure_status()
        self.__ensure_data()

    def __str__(self) -> str:
        return f"<Legym Response name='{self.__name}'>"

    def __repr__(self) -> str:
        return f"<Legym Response name='{self.__name}'>"

    def __parse_to_json(self) -> None:
        """Parse response to JSON form."""
        try:
            self.__body: dict = self.__response.json()
        except json.JSONDecodeError:
            raise LegymException(f"响应 {self.__name} 无法序列化：{self.__response.text}")

    def __ensure_status(self) -> None:
        """Ensure response status code equals 200."""
        status = self.__response.status_code
        if status == 200:
            return

        self.persist()
        raise LegymException(self.__body.get("message", f"网络异常，状态码：{status}"))

    def __ensure_data(self) -> None:
        """Ensure response JSON has key `data`."""
        if "data" in self.__body.keys():
            return

        self.persist()
        raise LegymException(f"响应 {self.__name} 没有 `data` 字段")

    def __getitem__(self, key: str):
        if key in self.__body.keys():
            return self.__body[key]

        if key in self.__body["data"].keys():
            return self.__body["data"][key]

        raise LegymException(f"{self.__name} API 的响应没有 `{key}` 字段")

    def persist(self, filepath: str = "") -> None:
        """Persist response JSON.

        Args:
            filepath: File path to persist the response, default to "",
            in which case response will be persisted as ".{self.__name}.json".

        Note:
            Mostly for debug purpose.
        """
        if filepath == "":
            filepath = f"{self.__name}.json"
        else:
            dirpath = os.path.dirname(filepath)
            if dirpath != "" and not os.path.exists(dirpath):
                os.mkdir(dirpath)

        with open(filepath, "w", encoding="utf-8") as fw:
            json.dump(self.__body, fw, ensure_ascii=False)
