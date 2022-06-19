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
fps = 240
# //////////////////////////////////////////////////////////////////////////////
ICON_image = Image.open(load_file("Icon/OPENGD.ico"))


# //////////////////////////////////////////////////////////////////////////////
def main(window_width, window_height):
    if not glfw.init():
        return
    # //////////////////////////////////////////////////////////////////////////////
    window = glfw.create_window(window_width, window_height, "OpenGD", None, None)
    glfw.set_window_icon(window, 1, ICON_image)
    glfw.set_window_aspect_ratio(window, 16, 9)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    # //////////////////////////////////////////////////////////////////////////////
    glEnable(GL_BLEND)
    glClear(GL_COLOR_BUFFER_BIT)
    glViewport(0, 0, window_width, window_height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # //////////////////////////////////////////////////////////////////////////////
    last_time = glfw.get_time()
    fps_previoustime = glfw.get_time()
    fps_framecount = 0
    while not glfw.window_should_close(window):
        glfw.poll_events()
        glfw.swap_buffers(window)
        # //////////////////////////////////////////////////////////////////////////////
        # frame_rate_limiter
        while glfw.get_time() < last_time + 1 / fps:
            pass
        last_time += 1 / fps
        # //////////////////////////////////////////////////////////////////////////////
        # fps
        fps_currentTime = glfw.get_time()
        fps_framecount += 1
        if fps_currentTime - fps_previoustime >= 1:
            print(fps_framecount)
            fps_framecount = 0
            fps_previoustime = fps_currentTime
        # //////////////////////////////////////////////////////////////////////////////
        v_width, v_height = glfw.get_window_size(window)
        glViewport(0, 0, v_width, v_height)
    glfw.destroy_window(window)
    glfw.terminate()


if __name__ == "__main__":
    main(1280, 720)
