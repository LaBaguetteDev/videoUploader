import json


class Server:
    def __init__(self):
        with open('ressources/serverinfo.json') as f:
            data = json.load(f)
            self._host = data['host']
            self._username = data['username']
            self._password = data['password']
            self._remote_path = data['remote_path']
            self._webbrowser_link = data['webbrowser_link']

    @property
    def host(self):
        return self._host

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def remote_path(self):
        return self._remote_path

    @property
    def webbrowser_link(self):
        return self._webbrowser_link
