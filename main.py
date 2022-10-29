
import pygame as pygame
import random as random
import numpy as np

from pygame.locals import *
from OpenGL.GL import  *
from OpenGL.GLU  import *




def main():
        pygame.init()
        display = (800, 550)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
        glTranslatef(-0.75, 0.0, -3)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            scale = 0.1

            glPointSize(2)

            #трехугольник
            glBegin(GL_TRIANGLES)
            glColor3ub(255, 0, 0)
            glVertex2f(1, 1)
            glVertex2f(1, -1)
            glVertex2f(-0.5, -1)

            glColor3ub(0, 255, 0)
            glVertex2f(-1, 1)
            glVertex2f(0.5, 1)
            glVertex2f(-1, -1)

            glEnd()

            #четырехугольник
            glBegin(GL_QUADS)

            glColor3ub(255, 255, 0)

            glVertex2f(-1, -1)
            glVertex2f(0.5, 1)
            glVertex2f(1, 1)
            glVertex2f(-0.5, -1)
            glEnd()


            pygame.display.flip()
            pygame.time.wait(1)

main()

