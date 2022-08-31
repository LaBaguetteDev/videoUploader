import tkinter as ttk
from model.video import Video
from view.view import View
from controller.videoController import VideoController


class App(ttk.Tk):
    def __init__(self):
        super().__init__()

        self.title('VideoUploader by LaBaguetteDev')
        self.geometry("540x100")
        self.resizable(False, False)
        # model
        video = Video('')

        # Vue
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # controller
        controller = VideoController(video, view)

        # controller de la vue
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()
