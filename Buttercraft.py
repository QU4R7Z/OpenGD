import os
import pyglet
from pyglet import gl

from Utils import jsonreader


def load_file(filename):
    return os.path.join(os.path.dirname(__file__), filename)


config = jsonreader.get(load_file("Config/config.json"))

# Font#######################################################################
pyglet.font.add_file(load_file("Font/GmarketSansTTFBold.ttf"))
GmarketSansTTFBold = pyglet.font.load('GmarketSansTTFBold', 48)
pyglet.font.add_file(load_file("Font/GmarketSansTTFMedium.ttf"))
GmarketSansTTFMedium = pyglet.font.load('GmarketSansTTFMedium', 48)
################################################################################

display = pyglet.canvas.Display()
screen = display.get_default_screen()
screen_width = screen.width
screen_height = screen.height
print(screen_width, screen_height)

glconfig = gl.Config(double_buffer=True)
window = pyglet.window.Window(1280, 720, "Buttercraft", resizable=False, fullscreen=True, config=glconfig)
window_icon = pyglet.image.load(load_file("Icon/Buttercraft.ico"))
window.set_icon(window_icon)

################################################################################
window_width = window.width
window_height = window.height


#################################################################################

versionlabel = pyglet.text.Label(f'Buttercraft {config.version}', font_name='Gmarket Sans TTF Medium',
                                 font_size=window_height / 30,
                                 x=window_width / 90, y=window_height / 42, anchor_x='left', anchor_y='baseline',
                                 color=(255, 255, 255, 255), width=200, height=100)

qu4r7zlabel = pyglet.text.Label(f'Copyright QU4R7Z. Do not Distribute!', font_name='Gmarket Sans TTF Medium',
                                font_size=window.height / 30,
                                x=window_width - window_width / 90, y=window_height / 42, anchor_x='right',
                                anchor_y='baseline',
                                color=(255, 255, 255, 255), width=200, height=100)


@window.event
def on_draw():
    window.clear()

    # BottomOverlayInfo##############################################################
    versionlabel.draw()
    qu4r7zlabel.draw()
    #################################################################################


if __name__ == '__main__':
    pyglet.app.run()
