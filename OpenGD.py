import os
import random
from array import array

import glfw
import numpy

from OpenGL.GL import *
from OpenGL.GLU import *
from Utils import jsonreader
from PIL import Image


# //////////////////////////////////////////////////////////////////////////////
def load_file(filename):
    return os.path.join(os.path.dirname(__file__), filename)


# //////////////////////////////////////////////////////////////////////////////
config = jsonreader.get(load_file("Config/config.json"))
fps = int(config.fps)
# //////////////////////////////////////////////////////////////////////////////
ICON_image = Image.open(load_file("Icon/OPENGD.ico"))


# //////////////////////////////////////////////////////////////////////////////
def main(window_width, window_height, dev=True):
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
    def loadTexture(texture):
        try:
            texx = Image.open(texture)
        except IOError as e:
            print("Failed to open texture file: ", texture)
            texx = Image.open(load_file("Resources/null.png"))

        texxData = list(texx.getdata())
        texxID = glGenTextures(1)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glBindTexture(GL_TEXTURE_2D, texxID)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_BORDER)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_BORDER)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_BASE_LEVEL, 0)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAX_LEVEL, 0)
        print(texx.size[0], texx.size[1])
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, texx.size[0], texx.size[1], 0, GL_RGBA, GL_UNSIGNED_BYTE, texxData)
        texx.close()
        return texxID

    def drawQuad(centerX, centerY, textureID, ratio):
        verts = ((ratio, ratio), (ratio, -ratio), (-ratio, -ratio), (-ratio, ratio))
        texts = ((1, 0), (1, 1), (0, 1), (0, 0))
        surf = (0, 1, 2, 3)

        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textureID)

        glBegin(GL_QUADS)
        for i in surf:
            glTexCoord2f(texts[i][0], texts[i][1])
            glVertex2f(centerX + verts[i][0], centerY + verts[i][1])
        glEnd()
        glDisable(GL_TEXTURE_2D)

    # //////////////////////////////////////////////////////////////////////////////
    sample_256_textureID = loadTexture(load_file("Resources/sample_256.png"))
    bg_textureID = loadTexture(load_file("Resources/bg_0_0_0_0_0_0.png"))

    # //////////////////////////////////////////////////////////////////////////////
    last_time = glfw.get_time()
    fps_previoustime = glfw.get_time()
    fps_framecount = 0
    # //////////////////////////////////////////////////////////////////////////////
    gluPerspective(45, (16 / 9), 0.1, 50.0)
    glTranslatef(0, 0, -5)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    # //////////////////////////////////////////////////////////////////////////////
    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        drawQuad(0, -1.4, bg_textureID, 6)
        drawQuad(glfw.get_time() - 12, -1.4, sample_256_textureID, 1)

        glfw.swap_buffers(window)
        # //////////////////////////////////////////////////////////////////////////////
        # frame_rate_limiter
        while glfw.get_time() <= last_time + 1 / fps:
            pass
        last_time += 1 / fps
        # //////////////////////////////////////////////////////////////////////////////
        # fps
        fps_currentTime = glfw.get_time()
        fps_framecount += 1
        if fps_currentTime - fps_previoustime >= 1:
            if dev:
                print(fps_framecount)
            fps_framecount = 0
            fps_previoustime = fps_currentTime
        # //////////////////////////////////////////////////////////////////////////////
        v_width, v_height = glfw.get_window_size(window)
        glViewport(0, 0, v_width, v_height)

    glfw.destroy_window(window)
    glfw.terminate()


if __name__ == "__main__":
    main(window_width=1280, window_height=720, dev=True)
