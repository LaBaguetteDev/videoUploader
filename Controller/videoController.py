class VideoController:
    def __init__(self, video, view):
        self.video = video
        self.view = view

    def upload(self, path):
        try:
            self.video.path = path
            self.video.upload()

            self.view.show_success('Success')

        except ValueError as e:
            self.view.show_error(e)