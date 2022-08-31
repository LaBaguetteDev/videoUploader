class VideoController:
    def __init__(self, video, view):
        self.video = video
        self.view = view

    def upload(self, path):
        try:
            self.video.path = path
            file_name, webbrowser_link = self.video.upload(self)

            self.view.show_success('Opération terminée')

            self.view.open_link(file_name, webbrowser_link)

        except:
            self.view.show_error('Une erreur est survenue')

    def print_progress(self, todo, done):
        self.view.show_progress(todo, done)
