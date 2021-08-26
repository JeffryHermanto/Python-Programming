# A Good Example of Inheritance

class InvalidOperationError(Exception):
    pass


class Stream:
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


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


fileStream = FileStream()
fileStream.open()
print(fileStream.opened)
fileStream.read()

networkStream = NetworkStream()
networkStream.open()
print(networkStream.opened)
networkStream.read()
