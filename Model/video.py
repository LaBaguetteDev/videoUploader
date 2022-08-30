from pystreamable import StreamableApi


class Video:
    def __init__(self, path, size):
        self._path = path
        self._size = size

    @property
    def path(self):
        return self._path

    @property
    def size(self):
        return self._size

    @path.setter
    def path(self, path):
        self._path = path

    @size.setter
    def size(self, size):
        self._size = size

    def upload(self):
        uploader = StreamableApi()
        result = uploader.upload_video(self._path, 'Test')
        print(result)