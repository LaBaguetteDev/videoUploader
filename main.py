import tkinter as ttk
from Model.video import Video
from View.view import View
from Controller.videoController import VideoController


class App(ttk.Tk):
    def __init__(self):
        super().__init__()

        self.title('VideoUploader by LaBaguetteDev')

        # Model
        video = Video('', 0)

        # Vue
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # Controller
        controller = VideoController(video, view)

        # Controller de la vue
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()
