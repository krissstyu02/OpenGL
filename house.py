import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
# The display() method does all the work; it has to call the appropriate
# OpenGL functions to actually display something.
def display():
    # Clear the color and depth buffers
    glClearColor(1, 1, 1, 1.0) # Тут цвет фона
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(5, 1 ,0.5, 0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    #отрисовка лицевой грани
    glColor3ub(227,38,54)
    glBegin(GL_QUADS)
    glVertex2f(0.5,0.5) 
    glVertex2f(0.5,-0.5) 
    glVertex2f(0.15,-0.5) 
    glVertex2f(0.15,0.5)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-0.15,0.5) 
    glVertex2f(-0.15,-0.5) 
    glVertex2f(-0.5,-0.5) 
    glVertex2f(-0.5,0.5)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(-0.15,0.5) 
    glVertex2f(-0.15,0.3) 
    glVertex2f(0.15,0.3) 
    glVertex2f(0.15,0.5)
    glEnd()
    #дверь
    glColor3ub(3,38,232)
    glBegin(GL_QUADS)
    glVertex2f(0.15,0.3) 
    glVertex2f(0.15,-0.5) 
    glVertex2f(-0.15,-0.5) 
    glVertex2f(-0.15,0.3)
    glEnd()
    #окно
    glColor3ub(0,50,54)
    glBegin(GL_QUADS)
    glVertex3f(0.53,-0.2,0.7)
    glVertex3f(0.53,0.2,0.7)
    glVertex3f(0.53,0.2,0.3)
    glVertex3f(0.53,-0.2,0.3)
    glEnd()
    glBegin(GL_QUADS)
    glVertex3f(-0.53,-0.2,0.7)
    glVertex3f(-0.53,0.2,0.7)
    glVertex3f(-0.53,0.2,0.3)
    glVertex3f(-0.53,-0.2,0.3)
    glEnd()
    #дальше
    glColor3ub(100,20,54)
    glBegin(GL_QUADS)
    glVertex3f(0.5,0.5,1)
    glVertex3f(0.5,-0.5,1)
    glVertex3f(0.5,-0.5,0)
    glVertex3f(0.5,0.5,0)
    glEnd()
    glColor3ub(100,20,10)
    glBegin(GL_QUADS)
    glVertex3f(-0.5,0.5,1)
    glVertex3f(-0.5,-0.5,1)
    glVertex3f(-0.5,-0.5,0)
    glVertex3f(-0.5,0.5,0)
    glEnd()
    glColor3ub(100,100,10)
    glBegin(GL_QUADS)
    glVertex3f(0.5,0.5,1)
    glVertex3f(0.5,-0.5,1)
    glVertex3f(-0.5,-0.5,1)
    glVertex3f(-0.5,0.5,1)
    glEnd()
    glColor3ub(230,100,10)
    glBegin(GL_QUADS)
    glVertex3f(-0.5,-0.5,0)
    glVertex3f(0.5,-0.5,0)
    glVertex3f(0.5,-0.5,1)
    glVertex3f(-0.5,-0.5,1)
    glEnd()
    #крыша :(
    glColor3ub(50,100,50)
    glBegin(GL_TRIANGLE_STRIP)
    glVertex3f(-0.5,0.5,0)
    glVertex3f(0.5,0.5,0)
    glVertex3f(0,1,0.5)
    glVertex3f(0.5,0.5,1)
    glVertex3f(-0.5,0.5,1)
    glVertex3f(0,1,0.5)
    glVertex3f(-0.5,0.5,0)
    glEnd()
    glutSwapBuffers()
    
def keyPressed(key,x,y):
    if key==b' ':
        display()

glutInit(sys.argv)

# Create a double-buffer RGBA window.   (Single-buffering is possible.
# So is creating an index-mode window.)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

# Create a window, setting its title
glutCreateWindow('interactive')

# Set the display callback.  You can set other callbacks for keyboard and
# mouse events.
glutDisplayFunc(display)
glutKeyboardFunc(keyPressed)
# Run the GLUT main loop until the user closes the window.
glutMainLoop()
