import pyglet

window = pyglet.window.Window(1280, 720, resizable=True)


@window.event
def on_resize(width, height):
    print(f"Window resized to ({width}, {height})")


if __name__ == '__main__':
    pyglet.app.run()
