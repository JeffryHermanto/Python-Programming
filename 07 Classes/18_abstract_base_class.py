# Abstract Base Class

from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self) -> None:
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream already open.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream already close.")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")
