import os

import pyglet


def load_file(filename: str):
    return os.path.join(os.path.dirname(__file__), filename)


window = pyglet.window.Window(1280, 720, "Buttercraft", resizable=True)
window_icon = pyglet.image.load(load_file("Resources/Icon/Buttercraft.ico"))
window.set_icon(window_icon)


@window.event
def on_resize(width, height):
    print(f"Window resized to ({width}, {height})")


if __name__ == '__main__':
    pyglet.app.run()
