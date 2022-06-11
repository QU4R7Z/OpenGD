import os
import pyglet
# //////////////////////////////////////////////////////////////////////////////
from pyglet.gl import *
from Utils import jsonreader


# //////////////////////////////////////////////////////////////////////////////
def load_file(filename):
    return os.path.join(os.path.dirname(__file__), filename)


# //////////////////////////////////////////////////////////////////////////////
config = jsonreader.get(load_file("Config/config.json"))
# //////////////////////////////////////////////////////////////////////////////
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
# //////////////////////////////////////////////////////////////////////////////
pyglet.font.add_file(load_file("Font/GmarketSansTTFBold.ttf"))
GmarketSansTTFBold = pyglet.font.load('GmarketSansTTFBold', 16)
pyglet.font.add_file(load_file("Font/GmarketSansTTFMedium.ttf"))
GmarketSansTTFMedium = pyglet.font.load('GmarketSansTTFMedium', 16)
pyglet.font.add_file(load_file("Font/GmarketSansTTFLight.ttf"))
GmarketSansTTFLight = pyglet.font.load('GmarketSansTTFLight', 16)
# //////////////////////////////////////////////////////////////////////////////
window = pyglet.window.Window(1280, 720, "Buttercraft", resizable=False, fullscreen=True)
window_icon = pyglet.image.load(load_file("Icon/Buttercraft.ico"))
window.set_icon(window_icon)
# //////////////////////////////////////////////////////////////////////////////
window_width = window.width
window_height = window.height
# //////////////////////////////////////////////////////////////////////////////
DESIRED_X_SIZE, DESIRED_Y_SIZE = window_height // 2, window_height // 2
QUARTZ_PNG = pyglet.image.load(load_file("Icon/quartz.png"))


# //////////////////////////////////////////////////////////////////////////////
@window.event
def on_resize(width, height):
    print(f"Window resized to ({width}, {height})")


# //////////////////////////////////////////////////////////////////////////////
versionlabel = pyglet.text.Label(f'Buttercraft {config.version}', font_name='Gmarket Sans TTF Medium',
                                 font_size=window_height / 30,
                                 x=window_width / 90, y=window_height / 42, anchor_x='left', anchor_y='baseline',
                                 color=(255, 255, 255, 255), width=200, height=100)
qu4r7zlabel = pyglet.text.Label(f'Copyright QU4R7Z. Do not Distribute!', font_name='Gmarket Sans TTF Medium',
                                font_size=window.height / 30,
                                x=window_width - window_width / 90, y=window_height / 42, anchor_x='right',
                                anchor_y='baseline',
                                color=(255, 255, 255, 255), width=200, height=100)


# //////////////////////////////////////////////////////////////////////////////
@window.event
def on_draw():
    window.clear()

    # //////////////////////////////////////////////////////////////////////////////
    versionlabel.draw()
    qu4r7zlabel.draw()
    # //////////////////////////////////////////////////////////////////////////////
    # SPLASH SCREEN
    QUARTZ_PNG.blit((window_width - QUARTZ_PNG.width) // 2, (window_height - QUARTZ_PNG.height) // 2, 0)
    # //////////////////////////////////////////////////////////////////////////////


if __name__ == '__main__':
    pyglet.app.run()
