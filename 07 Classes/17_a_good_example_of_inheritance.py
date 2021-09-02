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


file_stream = FileStream()
file_stream.open()
print(file_stream.opened)
file_stream.read()

network_stream = NetworkStream()
network_stream.open()
print(network_stream.opened)
network_stream.read()
