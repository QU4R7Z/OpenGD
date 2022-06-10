import os
import sys

import pygame

from Utils import jsonreader
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *


def load_file(filename):
    return os.path.join(os.path.dirname(__file__), filename)


config = jsonreader.get(load_file("Config/config.json"))
# //////////////////////////////////////////////////////////////////////////////
pygame.init()
icon = pygame.image.load(load_file("Icon/Buttercraft.png"))
pygame.display.set_icon(icon)
flags = DOUBLEBUF | FULLSCREEN | OPENGL
screen = pygame.display.set_mode((0, 0), flags)
screenx, screeny = screen.get_size()
pygame.display.set_caption("Buttercraft")
clock = pygame.time.Clock()
# //////////////////////////////////////////////////////////////////////////////
MediumFont = pygame.font.Font(load_file("Font/GmarketSansTTFMedium.ttf"), int(screeny/20))
BoldFont = pygame.font.Font(load_file("Font/GmarketSansTTFBold.ttf"), int(screeny/20))
LightFont = pygame.font.Font(load_file("Font/GmarketSansTTFLight.ttf"), int(screeny/20))
# //////////////////////////////////////////////////////////////////////////////
Loop = True
while Loop:
    events = pygame.event.get()
    if events:
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                Loop = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.MOUSEWHEEL:
                pass

    dt = clock.tick(60)
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    pygame.display.flip()

pygame.quit()
sys.exit()
