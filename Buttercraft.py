import os

import glfw
import numpy

from OpenGL.GL import *

from Utils import jsonreader
from PIL import Image


# //////////////////////////////////////////////////////////////////////////////
def load_file(filename):
    return os.path.join(os.path.dirname(__file__), filename)


# //////////////////////////////////////////////////////////////////////////////
config = jsonreader.get(load_file("Config/config.json"))

# //////////////////////////////////////////////////////////////////////////////
ICON_image = Image.open(load_file("Icon/Buttercraft.ico"))


# //////////////////////////////////////////////////////////////////////////////
def main():
    if not glfw.init():
        return
    # //////////////////////////////////////////////////////////////////////////////
    window = glfw.create_window(1280, 720, "Buttercraft", None, None)
    glfw.set_window_icon(window, 1, ICON_image)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    # //////////////////////////////////////////////////////////////////////////////\
    previousTime = glfw.get_time()
    framecount = 0
    while not glfw.window_should_close(window):
        currentTime = glfw.get_time()
        framecount += 1
        if (currentTime - previousTime) >= 1:
            print(framecount)
            framecount = 0
            previousTime = currentTime
        glfw.poll_events()
        glfw.swap_buffers(window)
    glfw.terminate()


if __name__ == "__main__":
    main()
