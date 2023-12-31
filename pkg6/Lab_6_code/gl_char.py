import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

vertices = (
    (-1.5, -0.5, -1.5),
    (-1.5, 0.5, -1.5),
    (-0.5, 0.5, -1.5),
    (-0.5, -0.5, -1.5),

    (0.5, -0.5, -1.5),
    (0.5, 0.5, -1.5),
    (1.5, 0.5, -1.5),
    (1.5, -0.5, -1.5),

    (-1.5, -0.5, 1.5),
    (-1.5, 0.5, 1.5),
    (-0.5, 0.5, 1.5),
    (-0.5, -0.5, 1.5),

    (0.5, -0.5, 1.5),
    (0.5, 0.5, 1.5),
    (1.5, 0.5, 1.5),
    (1.5, -0.5, 1.5),

    (-0.5, -0.5, 0),
    (-0.5, 0.5, 0),
    (0.5, 0.5, 0),
    (0.5, -0.5, 0)
)

edges = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),

    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),

    (0, 8),
    (1, 9),
    (2, 10),
    (3, 11),

    (8, 9),
    (9, 10),
    (10, 11),
    (11, 8),

    (12, 13),
    (13, 14),
    (14, 15),
    (15, 12),

    (4, 16),
    (5, 17),
    (6, 18),
    (7, 19),

    (12, 16),
    (13, 17),
    (14, 18),
    (15, 19)
)

def draw_axes():
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)  # X-axis (Red)
    glVertex3f(0, 0, 0)
    glVertex3f(1, 0, 0)
    glColor3f(0, 1, 0)  # Y-axis (Green)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 1, 0)
    glColor3f(0, 0, 1)  # Z-axis (Blue)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 1)
    glEnd()

def K():
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    clock = pygame.time.Clock()
    mouse_prev_pos = None
    scale_factor = 1.0
    translate_speed = 0.1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button pressed
                    mouse_prev_pos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button released
                    mouse_prev_pos = None
            elif event.type == pygame.MOUSEMOTION and mouse_prev_pos:
                x, y = event.pos
                dx, dy = x - mouse_prev_pos[0], y - mouse_prev_pos[1]
                mouse_prev_pos = (x, y)

                sensitivity = 0.2  # Adjust rotation sensitivity here
                glRotatef(dy * sensitivity, 1, 0, 0)
                glRotatef(dx * sensitivity, 0, 1, 0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_EQUALS:  # "+" key pressed
                    scale_factor += 0.001
                elif event.key == pygame.K_MINUS:  # "-" key pressed
                    scale_factor -= 0.001
                    if scale_factor < 0.1:
                        scale_factor = 0.1
                elif event.key == pygame.K_a:  # Left arrow key pressed
                    glTranslatef(-translate_speed, 0, 0)
                elif event.key == pygame.K_d:  # Right arrow key pressed
                    glTranslatef(translate_speed, 0, 0)
                elif event.key == pygame.K_s:  # Page Up key pressed
                    glTranslatef(0, 0, translate_speed)
                elif event.key == pygame.K_w:  # Page Down key pressed
                    glTranslatef(0, 0, -translate_speed)

        glScalef(scale_factor, scale_factor, scale_factor)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        K()
        draw_axes()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()