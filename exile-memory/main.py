import keyboard
import tkinter as tk
from importlib import resources
from glob import glob
from PIL import Image, ImageTk


class ExileMemory:

    image_labels = [
        'Edanna Entry',
        'Voltaic Entry',
        'Amateria Entry',
        'Amateria Pegs',
        'Amateria Final 1',
        'Amateria Final 2',
        'Amateria Final 3',
        'Amateria Chair',
        'First Poem (Top)',
        'First Poem (Bottom-Left)',
        'First Poem (Bottom-Right)',
        'Second Poem'
    ]

    def __init__(self):
        self.index = 0
        self.photo_image = None
        self.root = tk.Tk()
        self.images_path = resources.files('images')
        self.images = sorted(glob(str(self.images_path) + '/*.jpg'))
        self.image_label = tk.Label(self.root)
        self.image_label.grid(row=0)
        self.text_label = tk.Label(self.root)
        self.text_label.grid(row=1, pady=5)
        self.set_image()
        keyboard.hook(self.key_down)
        self.root.mainloop()

    def key_down(self, event) -> None:
        if type(event) == keyboard.KeyboardEvent and event.event_type == 'up':
            if event.name == 'o':
                self.back()
            elif event.name == 'p':
                self.forward()

    def set_image(self) -> None:
        image = str(self.images_path.joinpath(self.images[self.index]))
        open_image = Image.open(image)
        self.photo_image = ImageTk.PhotoImage(open_image)
        self.image_label.configure(image=self.photo_image)
        self.image_label.update()
        self.text_label.configure(text=self.image_labels[self.index])
        self.text_label.update()

    def back(self) -> None:
        if self.index != 0:
            self.index -= 1
        else:
            self.index = len(self.images) - 1

        self.set_image()

    def forward(self) -> None:
        if self.index != len(self.images) - 1:
            self.index += 1
        else:
            self.index = 0

        self.set_image()


ExileMemory()
