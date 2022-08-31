import pysftp

from model.server import Server


class Video:
    def __init__(self, path):
        self._path = path
        self._serverinfo = Server()

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    def upload(self, videocontroller):
        with pysftp.Connection(host=self._serverinfo.host,
                               username=self._serverinfo.username,
                               password=self._serverinfo.password) as sftp:
            file_name = self.path[self.path.rindex("/"):len(self.path)]

            remote_path = self._serverinfo.remote_path + file_name
            sftp.put(self.path, remote_path, callback=videocontroller.print_progress)

            return file_name, self._serverinfo.webbrowser_link

